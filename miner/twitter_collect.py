import time

import botornot
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys, getopt
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

host = "192.168.0.10"
port = 27017
dbName = "twitter"

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"h:p:d:",["host=","port=","dbname"])
    except getopt.GetoptError:
       print ('Help\n\n -h \t host= host ip \n -p \t port= mongoDb port\n -d \t dbname= MongoDb database Name')
       sys.exit(2)
    if len(opts) == 0:
       print('Help\n\n -h \t host= host ip \n -p \t port= mongoDb port\n -d \t dbname= MongoDb database Name')
       sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-d", "--dbname"):
            dbName = arg

if __name__ == "__main__":
   main(sys.argv[1:])

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
        db = MongoDb(host=host, dbName=dbName, port=port)
        print(db.find_tweet_by_id(db.insert_tweet(data)))
        time.sleep(6)
    # def on_event(self, status):
    #     print(status)

    def on_error(self, status_code):
        print(status_code)
        return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(languages=['en'],track=['python'], async=True)