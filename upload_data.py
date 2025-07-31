from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus



#url
name = "Himanshu"
password = "jaiswal@123"
encoded_password = quote_plus(password)
url = f"mongodb+srv://{name}:{encoded_password}@cluster0.8levazv.mongodb.net/?retryWrites=true&w=majority"


#create a new client connect to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"


df = pd.read_csv("wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

