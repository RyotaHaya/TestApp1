import responder
import handlers

api = responder.API(
    cors=True,
    cors_params={
        'allow_origins': ['*'],
        'allow_methods': ['*'],
        'allow_headers': ['*'],
    }
)


api.add_route('/', handlers.IndexController)
api.add_route('/hello', handlers.SampleClass)
api.add_route('/get', handlers.SampleGet)

api.add_route('/adminlogin', handlers.LoginController)

api.add_route('/api/twitter/requestToken', handlers.TwitterAuth)

# using tweepy
api.add_route('/api/homeTimelineMedia', handlers.TwitterHomeTimeLineMedia)
api.add_route('/api/listTimelineMedia', handlers.TwitterListTimeLineMedia)
api.add_route('/api/userFavMedia', handlers.TwitterUserFavMedia)
api.add_route('/api/userTimelineMedia', handlers.TwitterUserMedia)

# これはtwitter規約違反になりそうなのであまり使わない
api.add_route('/api/GetUserImageTweets', handlers.TwitterUserMedia)

if __name__ == '__main__':
   api.run(address='0.0.0.0', port=5042, debug=True)