from gcloud import datastore
import datetime
import json
# クライアントの設定
client = datastore.Client()

# エンティティ
key = client.key("media_tweets","0000000")
entity = datastore.Entity(key)

entity['created_date'] = datetime.datetime.now()
entity['user_id'] = 546546546545132
entity['user_screen_name'] = "watorin72"

image_keys =[]
# json.dumps(image_key_obj)
entity['media_keys'] = ["aaaa","dddddd"]
entity['media_type'] = "0"
entity['category'] = "0"

client.put(entity)
print("end")