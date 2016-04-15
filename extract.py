import re
from pymongo import MongoClient

def ExtractTweets(candidate):
    #Enter server details below:
    client=MongoClient('mongodb://z604_final:lanif_406z@45.33.57.4:27017/tweetDB')
    db=client["tweetDB"]
    collection = db[candidate]
    return [tweet for tweet in collection.find({"lang":"en"})]

#Applying simple regular expressions to just extract all the hashtags from the tweets
def ExtractHashtags(td):
    Hashtags={}
    for i in td.keys():
        Hashtags[i]=[]
        for j in range(len(td[i])):
            y=re.sub('\\n','',td[i][j]['text'])
            z=re.findall('#\w+',y)
            for x in z:
                Hashtags[i].append(x)
    return Hashtags