import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#twitter credentials
access_token = "719886346496643072-REHFkVrAz8M2gtYk09jDccbGKHcW68B"
access_token_secret = "b0B8ytTJcYXa3N1SKVgkI6KDOqu3hXIMc8JK4geMs7RrH"
consumer_key = "zDflY3b6jPGAw58NOmNxAiow9"
consumer_secret = "gSFCl8sRghqXFH2jQWpAnc7itUh9VbmrHL30dadybVvvaJcdiC"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#listener for handling tweets
class MyStreamListener(StreamListener):

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        print('')
        return True
    def on_error(self, status_code):
        print(status_code)
        return False



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['python'], async=True)