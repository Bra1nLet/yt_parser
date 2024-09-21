from pymongo import MongoClient
from src.config import MONGODB_CONNECTION_STRING

client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.get_database("youtube")

account_collection = db["account"]
proxy_collection = db["proxy"]

