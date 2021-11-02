import twitter
import datetime

class TweetDataManager:
    def get_user_media_tweet(self, user_id, all_get = False):
        try:
            gate = twitter.TwiterGateway()

            max_cnt = 1000

            req_list = []
            req_until = datetime.datetime.now() + datetime.timedelta(days=2)
            req_since = req_until - datetime.timedelta(weeks=12)

            span = 4
            #過去12年前までのツイートをする
            if all_get :
                span = 50

            #3か月単位で検索する
            for cnt in range(span):
                # 特定ユーザの画像ツイートIDを取得
                tweets_df = gate.get_user_image_tweets(
                    user_id, req_since.strftime('%Y-%m-%d'), req_until.strftime('%Y-%m-%d'), max_cnt)

                json = gate.conv_tweets_df_to_jsonList(tweets_df)
                if(len(json) > 0):
                    req_list.append(gate.conv_tweets_df_to_jsonList(tweets_df))
                else:
                    break
                req_until = req_since + datetime.timedelta(days=2)
                req_since = req_until - datetime.timedelta(weeks=12)

            ret_list = []
            id_list = []
            for list in req_list:

                sorted_list = sorted(list, reverse=True, key=lambda s: s["dateTime"])
                for tweet in sorted_list:
                    if not tweet["id"] in id_list:
                        id_list.append(tweet["id"])
                        ret_list.append(tweet)

            return ret_list

        except Exception as e:
            raise Exception(e)
