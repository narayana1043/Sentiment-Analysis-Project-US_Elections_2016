from extract import *
import nltk
import csv


#Calculating the hashtags frequency over the whole set of tweets for each candidate separately
def CalcHashFreq(ht):
    hf={}
    for i in ht.keys():
        hf[i]=nltk.FreqDist(ht[i])
    return hf

if __name__=='__main__':
    electionCandidates = ['HillaryClinton','JohnKasich','SenSanders','realDonaldTrump','tedcruz']
    tweetdict = {}
    for candidate in electionCandidates:
        tweetdict[candidate] = ExtractTweets(candidate)
    hashtags=ExtractHashtags(tweetdict)
    hashfreq=CalcHashFreq(hashtags)
    #Writing out the frequencies to a file to be used later
    with open('File.csv','w') as file:
        f=csv.writer(file)
        for i in hashfreq.keys():
            s=dict(hashfreq[i])
            file.write(i+'\n')
            for k,v in s.items():
                f.writerow([k,v])
