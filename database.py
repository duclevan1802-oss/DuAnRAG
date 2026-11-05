import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGODB_URL)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    db = client["fastapi_demo"]
    users_collection = db["users"]

except Exception as e:
    print("MongoDB connection failed!")
    print(e)