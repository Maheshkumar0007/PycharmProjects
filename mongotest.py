import pymongo

client = pymongo.MongoClient("mongodb+srv://mahesh:mahesh@cluster0.cobqgul.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "Mahesh",
    "email":"mbiradar@gmail.com",
    "surname":"Biradar"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)