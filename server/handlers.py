import responder
import twitter
import re
import batch_data_manager

# TODO パラメータの命名規則はキャメルケースを使用

api = responder.API()

class IndexController:
    async def on_get(self, req, resp):
        resp.content = api.template('index.html')

class LoginController:
    async def on_get(self, req, resp):
        resp.content = api.template('login.html')

class SampleClass:
    async def on_get(self, req, resp):
        # 何かしらの処理
        resp.text = "Hello root Page"


class SampleGet:
    async def on_get(self, req, resp):
        # 何かしらの処理
        resp.media = {
            "status": True,
            "result": "ss"
        }

class TwitterAuth:
    async def on_get(self, req, resp):
        try:
            gate = twitter.TwiterGateway()
            # 何かしらの処理
            token_url = gate.get_twitter_request_token()
            resp.media = {
                "url": token_url,
            }
        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
            "errors": [
            {
                "LocalizedMessage": str(e),
                "code": 500
            }
            ]
        }

class TwitterLogin:
    async def on_get(self, req, resp):
        # 何かしらの処理
        resp.media = {
            "status": True,
            "result": "ss"
        }

class TwitterHomeTimeLineMedia:
    async def on_get(self, req, resp):
        # 何かしらの処理
        try:
            # 返却するツイートデータ上限値
            max_count = int(req.params.get("maxCount", 50))

            # 取得範囲の指定(tweetIDを指定)
            max_id = req.params.get("maxId", "")
            since_id = req.params.get("sinceId", "")

            #　リツイートを含めるかどうか
            include_rts =  req.params.get("includeRtwees", True)

            # 検索範囲のツイート数(100~200推奨)
            range_count =  int(req.params.get("rangeCount", 100))

            gate = twitter.TwiterGateway()
            try:
                image_tweets = gate.get_home_timeline_media_tweets(max_count,since_id,max_id,include_rts,range_count)
            except Exception as e:
                raise Exception(e)

            resp.headers["Content-Type"] = "application/json; charset=UTF-8"
            resp.status_code = 200

            resp.media = {
                "UserId": "",
                "TotalCount": len(image_tweets),
                "ImageTweetList": image_tweets
            }

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "LocalizedMessage": str(e),
                        "StatusCode": resp.status_code
                    }
                ]
            }

class TwitterListTimeLineMedia:
    async def on_get(self, req, resp):
        # 何かしらの処理
        try:
            list_id = req.params.get("listId", "")

            if(list_id == ""):
                raise Exception("param ""listId"" is required.")

            # 返却するツイートデータ上限値
            max_count = int(req.params.get("maxCount", 50))

            # 取得範囲の指定(tweetIDを指定)
            max_id = req.params.get("maxId", "")
            since_id = req.params.get("sinceId", "")

            #　リツイートを含めるかどうか
            include_rts =  req.params.get("include_rts", False)

            # 検索範囲のツイート数(100~200推奨)
            range_count =  int(req.params.get("range_count", 100))

            gate = twitter.TwiterGateway()
            try:
                image_tweets = gate.get_list_timeline_media_tweets(max_count,list_id,since_id,max_id,include_rts,range_count)
            except Exception as e:
                raise Exception(e)

            resp.headers["Content-Type"] = "application/json; charset=UTF-8"
            resp.status_code = 200

            resp.media = {
                "UserId": "",
                "TotalCount": len(image_tweets),
                "ImageTweetList": image_tweets
            }

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "LocalizedMessage": str(e),
                        "StatusCode": resp.status_code
                    }
                ]
            }

class TwitterUserMedia:
    async def on_get(self, req, resp):

        try:
            user_id = req.params.get("userId", "")
            if(user_id == ""):
                raise Exception("param ""userId"" is required.")

            tweet_since = req.params.get("since", "")
            tweet_until = req.params.get("until", "")

            tweet_range = int(req.params.get("range", "50"))

            gate = twitter.TwiterGateway()
            # 特定ユーザの画像ツイートIDを取得
            image_tweets_list = gate.get_user_timeline_media_tweets(
                user_id, tweet_since, tweet_until, tweet_range)

            resp.headers["Content-Type"] = "application/json; charset=UTF-8"
            resp.status_code = 200

            resp.media = {
                "userId": user_id,
                "totalCount": len(image_tweets_list),
                "imageTweetId": image_tweets_list
            }

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "message": str(e),
                        "code": 500
                    }
                ]
            }

class TwitterUserMedia:
    async def on_get(self, req, resp):

        try:
            user_id = req.params.get("userId", "")
            if(user_id == ""):
                raise Exception("param ""userId"" is required.")

            date_since = req.params.get("since", "")
            date_until = req.params.get("until", "")
            max_cnt = int(req.params.get("maxCount", 0))

            gate = twitter.TwiterGateway()
            # 特定ユーザの画像ツイートIDを取得
            image_tweets_list = gate.get_user_image_tweets(
                user_id, date_since, date_until, max_cnt)

            resp.headers["Content-Type"] = "application/json; charset=UTF-8"
            resp.status_code = 200

            resp.media = {
                "userId": user_id,
                "totalCount": len(image_tweets_list),
                "imageTweetId": image_tweets_list
            }

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "message": str(e),
                        "code": 500
                    }
                ]
            }


class TwitterUserFavMedia:
    async def on_get(self, req, resp):

        try:

            oauth = req.headers["Authorization"]
            token_list = re.split('\s', oauth)

            token_list = re.split('\s', oauth)
            token = token_list[1]
            token_secret = token_list[2]

            user_id = req.params.get("userId", "")

            if(user_id == ""):
                raise Exception("param ""userId"" is required.")

            max_cnt = int(req.params.get("maxCount", 100))

            exe_identifies_image = req.params.get("identifieImage", "")

            gate = twitter.TwiterGateway()
            # 特定ユーザの画像ツイートIDを取得
            if exe_identifies_image == "yes" :
                identifies_image_size = req.params.get("imageSIze", "small")
                image_tweets = gate.get_identified_user_favlist(user_id, max_cnt, identifies_image_size)
            else :
                image_tweets = gate.get_user_favlist(user_id, max_cnt)


            resp.media = {
                "userId": user_id,
                "totalCount": len(image_tweets),
                "imageTweetId": image_tweets
            }

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "message": str(e),
                        "code": 500
                    }
                ]
            }

class BatchTweet:
    async def on_post(self, req, resp):

        try:
            a = batch_data_manager.TwitterUserImages
            tweets = a.get_image_tweet("watorin72")

            print(len(tweets))

            for tweet in tweets:
                print(str(tweet["id"] ))

        except Exception as e:
            resp.status_code = api.status_codes. HTTP_500

            resp.media = {
                "errors": [
                    {
                        "message": str(e),
                        "code": 500
                    }
                ]
            }
