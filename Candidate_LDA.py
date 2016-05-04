import re
from nltk.corpus import stopwords
from gensim import corpora,models
from pprint import pprint

def ReadData(filename):
    speech=[]
    with open(filename,'r') as f:
        line=f.readline()
        speech.append(line)
        for line in f:
            #c=f.readline()
           speech.append(line)
    return speech


def LDA(candidate):
    sw=set(stopwords.words("english"))
    sw.add("rt")


    for i in range(len(candidate)):
        x=re.findall(r"\w+'?[a-z]",candidate[i])
        x=set([word.lower() for word in x])
        candidate[i]=x-sw
        
    dictionary=corpora.Dictionary(candidate)
    corpus=[dictionary.doc2bow(text) for text in candidate]
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=10, id2word = dictionary)
    return ldamodel
    
# hillary=ReadData('Hillary Clinton Calls for Universal Preschool.txt')
# ldahillary=LDA(hillary)
# pprint(ldahillary.print_topics(num_topics=2))

bernie=ReadData('bernie.txt')
ldabernie=LDA(bernie)
pprint(ldabernie.print_topics(num_topics=10))

#
# trump=ReadData('')
# ldatrump=LDA(trump)
#
# cruz=ReadData('')
# ldacruz=LDA(cruz)
#
# kasich=ReadData('')
# ldakasich=LDA(kasich)
