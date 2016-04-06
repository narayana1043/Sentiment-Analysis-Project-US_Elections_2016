''' Naming Conventions

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

mixedCase is allowed only in contexts where that's already the prevailing style

Variables = camelCase

'''

import tweepy
from pymongo import MongoClient
import json

#linking the api account keys
consumer_key = ""                                       #consumer token
consumer_secret=""                                      #consumer secret
access_token = ""                                       #access token
access_secret=""                                        #access secret

# creating an OAuthHandler Instance
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

#equpping OAuthHandler with access token
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

#creating Mongo Client #alternative: client = MongoClient('mongodb://localhost:27017/')
#client = MongoClient('localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")
db = client['tweetDB']
collections = db['trump']

for status in tweepy.Cursor(api.user_timeline,id="realDonaldTrump").items(1):
    collections.insert_one(status._json)

client.close()


