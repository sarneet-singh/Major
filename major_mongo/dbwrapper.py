from pymongo import MongoClient


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MongoDb():
    global host
    global port
    global client
    global db

    def __init__(self, host, port, dbName):
        super().__init__()
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        self.db = self.client[dbName]

    def insert_tweet(self, data):
        return self.db['tweets'].insert_one(data).inserted_id

    def find_tweet_by_id(self, id):
        return self.db['tweets'].find_one({"_id": id})
