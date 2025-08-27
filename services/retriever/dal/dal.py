from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
from services.retriever.urils.utils_function import convert_bson_types


class DAL:
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

    def get_all_data(self):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            # Return all documents
            res = list(collection.find({}).limit(5))
            return res




