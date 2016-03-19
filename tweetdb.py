import tweepy
import pymongo
from pymongo import MongoClient
import json

#linking the api account keys
consumer_key = "URKEq38uEfEBYJKhtJsulCkT3"                                      #consumer token
consumer_secret="R7Ura3hXyreftZsFlesQ0eMMUopxRbfvVxBG6qlbzDQH87MjD8"            #consumer secret
access_token = "574211833-xxYFY0RXSDfgfpGCTV4MjLeyaKpfu1YWw8KOJSUP"             #access token
access_secret="8NwigwWy8hcFaeEDMtQALQCRp1BUYUALruF68sFpR3ucr"                   #access secret

# creating an OAuthHandler Instance
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

#equpping OAuthHandler with access token
auth.set_access_token(access_token,access_secret)

#creating Mongo Client
client = MongoClient('localhost', 27017)