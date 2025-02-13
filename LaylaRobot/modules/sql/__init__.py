import os

DB_URI = os.environ.get("DB_URI")  # Get the MongoDB URI from environment variables

# 🔥 Debugging: Print DB_URI
print(f"🔍 DB_URI: {DB_URI}")  # Add this line

if not DB_URI:
    raise ValueError("🚨 ERROR: DB_URI is empty! Please check your environment variables.")

from pymongo import MongoClient

client = MongoClient(DB_URI)  # Connect to MongoDB
database = client.get_database()  # Get the default database
