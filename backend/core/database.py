import time
from pymongo import MongoClient


from backend.core.config import Config


def get_client(retries: int = 5, delay: int = 2) -> MongoClient:
    for attempt in range(1, retries + 1):
        try:
            client = MongoClient(Config.MongoClientURI, serverSelectionTimeoutMS=3000)

            client.admin.command("ping")

            return client

        except Exception as e:
            print(f"Attempt {attempt}/{retries} failed: {e}")

            if attempt == retries:
                raise RuntimeError("MongoDB connection failed after retries")

            time.sleep(delay)

    raise Exception  # For type check


mongo_client = get_client()

BMS = mongo_client.get_database(Config.DBName)

users_collection = BMS["users"]
items_collection = BMS["items"]
bills_collection = BMS["bills"]


def is_db_alive() -> bool:
    try:
        mongo_client.admin.command("ping")
        return True
    except Exception:
        return False
