from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client['Electiondb']
collection=db['Testcollection']
hillaryTweets=[tweet for tweet in collection.find({"user.screen_name":"HillaryClinton"})]
trumpTweets=[tweet for tweet in collection.find({"user.screen_name":"realDonaldTrump"})]
cruzTweets=[tweet for tweet in collection.find({"user.screen_name":"tedcruz"})]
sandersTweets=[tweet for tweet in collection.find({"user.screen_name":"SenSanders"})]