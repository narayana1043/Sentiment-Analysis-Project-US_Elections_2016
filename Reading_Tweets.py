from pymongo import MongoClient

#This should be updated to reflect the server our MongoDB is on

client=MongoClient('localhost',27017)
db=client['Electiondb']

#Idea is to have a single collection for all the tweets. See below to access tweets from a particular candidate.
collection=db['Testcollection']

#Creating a list of dictionaries for each tweet.
#hillaryTweets[0]['text'] would give out text, similarly other tags will give other details, ex: geo,created_at,favourite_count etc.
hillaryTweets=[tweet for tweet in collection.find({"user.screen_name":"HillaryClinton"})]
trumpTweets=[tweet for tweet in collection.find({"user.screen_name":"realDonaldTrump"})]
cruzTweets=[tweet for tweet in collection.find({"user.screen_name":"tedcruz"})]
sandersTweets=[tweet for tweet in collection.find({"user.screen_name":"SenSanders"})]
