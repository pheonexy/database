import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


myquery1 = { "city": { "$gt": "S" } } #start greater than 

myquery2 = {"city" : {"$regex": "^O"}} #start wiith s

mydoc1 = mycol.find(myquery1)
for x in mydoc1:
  print(x)
  
mydoc2 = mycol.find(myquery2)
for y in mydoc2:
  print(y)
