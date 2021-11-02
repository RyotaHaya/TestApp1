import csv
from urllib import parse
import datetime
import os
import sys
import glob
import datetime
import os, sys
from gcloud import datastore
import shutil

p = os.path.abspath('.')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import twitter
import identifies_image

class csv_manger:
    def get(self,path):
        file = open(path,'r',encoding="utf-8")
        f = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        line = [row for row in f]
        header = line[5]
        cnt = 0

        list = []
        for i in range(6, len(line)):
            #6行からデータ開始
            created_date_str = line[i][0]
            created_date = datetime.datetime.strptime(created_date_str, '%Y/%m/%d %H:%M:%S') 
            #created_date = datetime.datetime.strptime(jst_created_date, '%Y/%m/%d %H:%M:%S') - datetime.timedelta(hours=9)

            user_id = "" 
            user_screen_name = line[i][3]
            user_screen_name = user_screen_name.replace("@","")

            tweet_url = line[i][4]
            id = tweet_url.replace('https://twitter.com/'+user_screen_name+'/status/', '')

            #0:静止画　1:動画　2:GIF
            media_type =0 
            media_type_str = line[i][5]
            if media_type_str == "Video":
                media_type = 1
            elif media_type_str == "GIF":
                media_type = 2

            media_urls = line[i][6]
            media_url_entities = parse.urlparse(media_urls)
            
            media_keys = [] 
            media_keys = [] 

            if media_type == 0:
                media_keys.append(str(media_url_entities.path).replace("/media/",""))
            elif media_type == 1:
                media_keys.append(str(media_url_entities.path).replace("/ext_tw_video/",""))
            elif media_type == 2:
                media_keys.append(str(media_url_entities.path).replace("/tweet_video/",""))

            media_formats = []
            if media_type_str == "Image":
                qs_d  = parse.parse_qs(media_url_entities.query)
                media_formats.append(str(qs_d["format"][0]))

            #同一ツイートの検索

            if not i+1 == len(line):
                for j in range(i + 1, i + 3) :

                    if  not j+1 == len(line):

                        next_url = line[j][4]
                        next_id = next_url.replace('https://twitter.com/'+user_screen_name+'/status/', '')

                        if id == next_id:
                            next_media_urls = line[j][6]
                            next_media_url_entities = parse.urlparse(next_media_urls)
                            media_keys.append(str(next_media_url_entities.path).replace("/media/",""))
                            
                            if media_type == 0:
                                next_qs_d  = parse.parse_qs(next_media_url_entities.query)
                                media_formats.append(str(next_qs_d["format"][0]))
                        else:
                            break
                    else:
                        break

            json_obj = {
                "id":id,
                "user_id":user_id,
                "user_screen_name":user_screen_name,
                "created_date":created_date,
                "media_type":media_type,
                "media_formats":media_formats,               
                "media_keys":media_keys,
            }

            list.append(json_obj)

            # インクリメント
            i = i + len(media_keys) -1 
        
        return list
            
if __name__ == '__main__':
    csv_manage = csv_manger()

    target_path = "C:/Users//User/Desktop/csvWorks/"
    target_path = str(target_path).translate(str.maketrans('/', '\\'))

    dest_path = target_path + '\\result\\'
    os.makedirs(dest_path, exist_ok=True)

    targetfiles = []


    files = glob.glob(target_path + ""+ "*." + "csv")
    targetfiles.extend(files)

    if(len(targetfiles) == 0) :
        print('csvファイルが存在しません。')
        exit()

    gate = twitter.TwiterGateway()
    # クライアントの設定
    client = datastore.Client()
    try:
        for file in targetfiles:
            target_list = csv_manage.get(file)

            user_screen_name = target_list[0]["user_screen_name"]

            user_profile = gate.get_user_profile(user_screen_name)

            for list in target_list:
                # エンティティ
                key = client.key("media_tweets",list["id"])
                entity = datastore.Entity(key)

                entity['created_date'] = list["created_date"]
                entity['user_id'] = str(user_profile.id)
                entity['user_screen_name'] = user_screen_name

                image_keys =[]
                # json.dumps(image_key_obj)
                entity['media_keys'] = list["media_keys"]
                entity['media_type'] = list["media_type"]

                category = 0

                #0:静止画　1:動画　2:GIF
                if list["media_type"] == 0:
                    
                    #gifは判定しない
                    if(list["media_formats"][0] =="png" or list["media_formats"][0] =="jpg"):
                        url = "https://pbs.twimg.com/media/" + list["media_keys"][0] +"?format=" +list["media_formats"][0]+ "&name=small"
                        is_illust_work = identifies_image.do_identifiesImage(url)
                        if is_illust_work:
                            category = 1
                else:
                    #動画はその他へ分類
                    category = 9
                #0:写真　1:イラスト　       9:その他
                entity['category'] = category

                entity['gcp_vision_api_done'] = False
                client.put(entity)
                print("USER:" + user_screen_name + " TweetID =" +  str(list["id"]) + " was created!")

            #target_path = "C:/Users//User/Desktop/csvWorks/"
            shutil.move(file, target_path + "done")

    except Exception as e:
        print(e)

    print("end---------------------------------------------------------------------------------------------------------")
