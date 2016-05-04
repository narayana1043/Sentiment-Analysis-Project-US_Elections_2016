from pymongo import MongoClient as MC
from nltk.corpus import stopwords
from gensim import corpora,models
import numpy
import re
import time
import logging
import pickle

start=time.time()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def ExtractTweets(user,conn,dbname):
    #Enter server details below:
    client=MC(conn)
    db=client[dbname]
    #Candidates tweets to extract from MongoDB
    td=[]
    #Creating a dictionary to hold all the tweets from the presidential candidates
    collection=db[user]
    #We care only for english tweets, hence the language filter
    print("connected")
    td1=[tweet['text'] for tweet in collection.find({"lang":"en"})]
    td.extend(td1)
    print("extracted")
    return td

sw=set(stopwords.words("english"))
sw.add("rt")
# conn_string =''
# user_des=ExtractTweets('tweetStream',conn_string,'tweetDB')
#
# pickle.dump(user_des, file=open("user_des_tweets", "wb"))

user_des = pickle.load(file=open("user_des_tweets", "rb"))

print("extraction for")
for i in range(len(user_des)):

    user_des[i]=re.sub('\s?http(\w+|:)\W+.+','',user_des[i])
    user_des[i]=re.sub('@\w+','',user_des[i])

print("2nd for")
for i in range(len(user_des)):

    x=re.findall(r"\w+'?[a-z]",user_des[i])
    x=set([word.lower() for word in x])
    user_des[i]=x-sw

print("came here")
dictionary=corpora.Dictionary(user_des)
corpus=[dictionary.doc2bow(text) for text in user_des]
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=10)
print(ldamodel.print_topics(num_topics=5))
