from pymongo import MongoClient
import os
from dotenv import load_dotenv


class Dal:
    """Retrieve documents from a MongoDB collection."""

    load_dotenv()

    def __init__(self):
        self.USER = os.getenv("USER")
        self.DB_NAME = os.getenv("DB_NAME")
        self.PASS = os.getenv("PASS")
        self.COLLECTION = os.getenv("COLLECTION")
        self.MONGO_URI = os.getenv("MONGO_URI")


        # Check if any critical environment variables are missing
        missing = [
            name for name, val in [
                ("USER", self.USER),
                ("PASS", self.PASS),
                ("DB_NAME", self.DB_NAME),
            ] if not val
        ]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        # Build the MongoDB connection URI
        self.MONGO_URI = (self.MONGO_URI)

    def get_data(self, counter):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            raw_data = list(collection.find({}).sort("CreateDate").skip(counter).limit(100))
            return raw_data

