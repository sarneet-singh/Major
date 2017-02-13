import time

import botornot
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from major_mongo.dbwrapper import MongoDb

access_token = "719886346496643072-REHFkVrAz8M2gtYk09jDccbGKHcW68B"
access_token_secret = "b0B8ytTJcYXa3N1SKVgkI6KDOqu3hXIMc8JK4geMs7RrH"
consumer_key = "zDflY3b6jPGAw58NOmNxAiow9"
consumer_secret = "gSFCl8sRghqXFH2jQWpAnc7itUh9VbmrHL30dadybVvvaJcdiC"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }

bon = botornot.BotOrNot(**twitter_app_auth)

#listener for handling tweets
class MyStreamListener(StreamListener):


    # def add_bot_or_not_data(jsonData):
    #     if(jsonData.has_key(''))
    #
    #
    # def on_data(self, data):
    #     # Twitter returns data in JSON format - we need to decode it first
    #     decoded = json.loads(data)
    #     # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
    #     print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
    #
    #     #print(MongoDb().find_tweet_by_id(MongoDb().insert_tweet(decoded)))
    #
    #     print('')
    #     return True

    def on_status(self, status):
        data = status._json
        print(MongoDb().find_tweet_by_id(MongoDb().insert_tweet(data)))
        time.sleep(6)
    # def on_event(self, status):
    #     print(status)

    def on_error(self, status_code):
        print(status_code)
        return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(languages=['en'],track=['python'], async=True)