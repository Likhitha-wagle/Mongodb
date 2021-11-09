from pymongo import MongoClient
import json

# for connecting to mongodb and create database named mydatabase
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient['mydatabase']
collection = db.mydatabase

print("enter json data to insert into table")
inp=input()

print("enter the value to find all record containing that value")
value=input()

print("enter field to select record will return all fields")
field=input()

print("enter key value pair to delete")
delete=input()

# insert records
if inp=='':
    print("not entered any data to insert")
else:
    inp1=json.loads(inp)
    rec_id1 = collection.insert_one(inp1)
    print("Data inserted")
    print(inp1)

# get record for particular value
cursor = collection.find()
if value=='':
    print("Not entered any data to get values")
else:
    for record in cursor:
        for i,v in record.items(): 
            if v==value:
                print("Values present for"" "+value+" ""are")
                print(record)
                
# for getting field data
cursor = collection.find() 
for record in cursor:
    if field=='':
        print("field data")
        print(record)
    for i,v in record.items():
        if i==field:
            print("field data for"" "+field+" ""is:")
            print(record[i]) 

# delete records
cursor = collection.find()
if delete=='':
    print("Not entered any data to delete")
else:
    delete1=json.loads(delete)
    for record in cursor:
        for i,v in record.items():
            for j,k in delete1.items():
                if k==v:
                    collection.delete_many(delete1)
                    print("Data with key"" "+j+" ""value"" "+k+" ""is deleted")