import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()
print(x)

for x in mycol.find({},{"_id":0, "name":1, "city":1}):
    print(x)
    
for x in mycol.find({},{ "city": 0 }):
    print(x)
    
for x in mycol.find({},{ "name": 1, "city": 0 }): #error
    print(x)
    
myquery = { "city": "Lowstreet" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
