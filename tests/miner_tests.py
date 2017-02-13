from pymongo import MongoClient

def setup():
    print("SETUP!")
def teardown():
    print("TEAR DOWN!")
def test_basic():
    print("I RAN")

MongoClient(host="192.168.0.10",port=27017).twitter.tweet.insert_one({"yo": "yo"})

