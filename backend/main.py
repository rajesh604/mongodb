import pymongo
import json

# Connect to MongoDB inside the Docker container
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Load JSON data from file
with open("jsondata.json") as f:
    data = json.load(f)

# Insert data into MongoDB collection
db = client["mydatabase"]
collection = db["mycollection"]
# collection.insert_many(data)

# Print the number of documents in the collection
# print(f"{collection.count_documents({})} documents in collection")

results = collection.find({"sector":"Energy"})

i = 0

for result in results:
    i += 1
    print(result)

print(i)