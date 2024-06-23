#inserting ramdon values for the database

from pymongo import MongoClient

import random
import string

client= MongoClient('mongodb://localhost:28000')

db=client['twitter']
tweets=db['tweets']
tweets.drop()

usuarios=[("bertoldo",1320),("herminia",5320),("aniceto",123),("meliba",411),("franco",2234)]
n=100

for i in range(1,n+1):
  tweet={}
  tweet['_id']=i
  tweet['text']= ''.join(random.choices(string.ascii_uppercase,k=10))
  u={}
  u['nick'],u['followers']=random.choice(usuarios)
  tweet['usuario']=u
  tweet['RT']= i>1 and random.choice([False,True])
  if tweet['RT'] and i>1:
    tweet['origen']= random.randrange(1,i)
  m=random.sample(usuarios, random.randrange(0, len(usuarios)))
  tweet['mentions']=[nick for nick, _ in m]
  tweets.insert_one(tweet)

