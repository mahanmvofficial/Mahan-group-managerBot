import threading
from pymongo import MongoClient
import os

# Connect to MongoDB
DB_URI = os.getenv("DB_URI")  # Ensure DB_URI is set in your environment
if not DB_URI:
    raise ValueError("DB_URI is missing! Check your environment variables.")

client = MongoClient(DB_URI)
database = client.get_database()
blacklist_users = database.blacklist_users  # MongoDB Collection

BLACKLIST_LOCK = threading.RLock()
BLACKLIST_USERS = set()

def blacklist_user(user_id, reason=None):
    """Add a user to the blacklist."""
    with BLACKLIST_LOCK:
        blacklist_users.update_one(
            {"user_id": str(user_id)}, 
            {"$set": {"reason": reason}}, 
            upsert=True
        )
        __load_blacklist_userid_list()

def unblacklist_user(user_id):
    """Remove a user from the blacklist."""
    with BLACKLIST_LOCK:
        blacklist_users.delete_one({"user_id": str(user_id)})
        __load_blacklist_userid_list()

def get_reason(user_id):
    """Get the reason why a user is blacklisted."""
    user = blacklist_users.find_one({"user_id": str(user_id)})
    return user["reason"] if user else ""

def is_user_blacklisted(user_id):
    """Check if a user is blacklisted."""
    return str(user_id) in BLACKLIST_USERS

def __load_blacklist_userid_list():
    """Load all blacklisted users into a set."""
    global BLACKLIST_USERS
    BLACKLIST_USERS = {x["user_id"] for x in blacklist_users.find()}
    
__load_blacklist_userid_list()
