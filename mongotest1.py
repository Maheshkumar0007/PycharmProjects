import pymongo

client = pymongo.MongoClient("mongodb+srv://mahesh:mahesh@cluster0.cobqgul.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

list_of_records=[
    {"name": "Rajesh",
    "email":"rajeshbiradar1995@gmail.com",
    "surname":"Biradar","age":"27"},

    {"name": "Dinesh",
    "email":"Dineshbiradar@gmail.com",
    "surname":"Biradar","age":"29"},
    {"name": "Mahesh",
     "email": "mbiradar@gmail.com",
     "surname": "Biradar","age":"25"}
]
db1=client['mongotest1']
coll=db1['test1']
coll.insert_many(list_of_records)

data=coll.find()
for i in data:
    print(i)