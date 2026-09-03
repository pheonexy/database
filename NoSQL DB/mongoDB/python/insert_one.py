import pymongo as pm

myclient = pm.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {"name":"John", "city":"Highway"}

x= mycol.insert_one(mydict)

print(f"the element {x.inserted_id} is inserted")
