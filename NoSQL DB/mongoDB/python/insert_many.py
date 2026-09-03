import pymongo as pm

myclient = pm.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"]

mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "city": "Apple st 652"},
  { "name": "Hannah", "city": "Mountain 21"},
  { "name": "Michael", "city": "Valley 345"},
  { "name": "Sandy", "city": "Ocean blvd 2"},
  { "name": "Betty", "city": "Green Grass 1"},
  { "name": "Richard", "city": "Sky st 331"},
  { "name": "Susan", "city": "One way 98"},
  { "name": "Vicky", "city": "Yellow Garden 2"},
  { "name": "Ben", "city": "Park Lane 38"},
  { "name": "William", "city": "Central st 954"},
  { "name": "Chuck", "city": "Main Road 989"},
  { "name": "Viola", "city": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
