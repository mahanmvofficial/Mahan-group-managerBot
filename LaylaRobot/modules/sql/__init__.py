from pymongo import MongoClient
import os

DB_URI = os.environ.get("DB_URI")  # Get MongoDB URI from environment variables

if not DB_URI:
    raise ValueError("DB_URI is not set. Please set it in environment variables.")

client = MongoClient(DB_URI)  # Connect to MongoDB
db = client.get_database()  # Get the default database
