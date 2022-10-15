import pymongo

client = pymongo.MongoClient("mongodb+srv://mahesh:mahesh@cluster0.cobqgul.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
db1=client['mongotest1']
coll=db1['test1']
data=coll.find()
print("output after putting search option blank")
for i in data:
    print(i)


#this find function is having case sesitivity , if we enter same text with different case it will not give correct output

print("output after putting some search condition")
data2=coll.find({"name":"Mahesh"})
for i in data2:
    print(i)

print("output after applying filters that values of name sholuld be greater than equal to E")


#output after applying filter as name value having greater than or equals to E

data3=coll.find({"name":{"$gt":"E"}})
for i in data3:
    print(i)

#output after applying filter as name value having either 'Mahesh' or 'Rajesh'

print("output after applying filters that values of name should be either Mahesh or Rajesh")
data4=coll.find({"name":{"$in":["Mahesh","Rajesh"]}})
for i in data4:
    print(i)

#output after greater than equal to filter for numerical value

print("output after applying filters that values of age should be greater than equal to 27")
data5=coll.find({'age':{'$gte':'27'}})
for i in data5:
    print(i)