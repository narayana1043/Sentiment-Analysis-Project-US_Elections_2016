''' Naming Conventions

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

mixedCase is allowed only in contexts where that's already the prevailing style

Variables = camelCase

'''

import tweepy
from pymongo import MongoClient
import json

#linking the api account keys
consumer_key = "URKEq38uEfEBYJKhtJsulCkT3"                                      #consumer token
consumer_secret="R7Ura3hXyreftZsFlesQ0eMMUopxRbfvVxBG6qlbzDQH87MjD8"            #consumer secret
access_token = "574211833-xxYFY0RXSDfgfpGCTV4MjLeyaKpfu1YWw8KOJSUP"             #access token
access_secret="8NwigwWy8hcFaeEDMtQALQCRp1BUYUALruF68sFpR3ucr"                   #access secret

# creating an OAuthHandler Instance
auth=OAuthHandler(consumer_key,consumer_secret)

#equpping OAuthHandler with access token
auth.set_access_token(access_token,access_secret)

#creating Mongo Client #alternative: client = MongoClient('mongodb://localhost:27017/')
client=MongoClient('localhost',27017)

#Setting up DB and collection:
db=client['Electiondb']
collection=db['Testcollection']

api=tweepy.API(auth)

#Might have to add exception handling to address timing issue
for status in tweepy.Cursor(api.user_timeline,id='realDonaldTrump').items(1000):
    collection.insert(status._json)
    
for status in tweepy.Cursor(api.user_timeline,id='HillaryClinton').items(1000):
    collection.insert(status._json)
    
for status in tweepy.Cursor(api.user_timeline,id='tedcruz').items(1000):
    collection.insert(status._json)
    
for status in tweepy.Cursor(api.user_timeline,id='SenSanders').items(1000):
    collection.insert(status._json)

client.close()


