from pymongo import MongoClient
client = MongoClient('mongodb://localhost:28000')

db=client['twitter']
tweets=db['tweets']

tweet={
  '_id':2,
  'usuario':{'nick':"hermenia",'seguidores':5320},
  'texto':"RT:@hermenia: hoy, excursión a la sierra con @aniceto",
  'menciones':["hermenia","aniceto"],
  'RT':True,
  'origin':1
}
insert= tweets.insert_one(tweet)

print(insert.inserted_id)