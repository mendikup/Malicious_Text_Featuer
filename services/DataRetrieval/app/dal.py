from pymongo import MongoClient
import os
from utils import convert_bson_types


class Dal:
    """Retrieve documents from MongoDB collections."""

    def __init__(self) -> None:
        self.ANTISEMITIC_COLLECTION = os.getenv(
            "ANTISEMITIC_COLLECTION", "tweets_antisemitic"
        )
        self.NOT_ANTISEMITIC_COLLECTION = os.getenv(
            "NOT_ANTISEMITIC_COLLECTION", "tweets_not_antisemitic"
        )
        self.DB_NAME = os.getenv("MONGO_DB", "mydb")
        self.MY_MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")


    def get_not_antisemitic_data(self):
        """Return a sample of non-antisemitic documents."""
        with MongoClient(self.MY_MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.NOT_ANTISEMITIC_COLLECTION]
            data = list (collection.find({}).limit(100))
            data = convert_bson_types(data)
            return data



    def get_antisemitic_data(self):
        """Return a sample of antisemitic documents."""
        with MongoClient(self.MY_MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.ANTISEMITIC_COLLECTION]
            data = list(collection.find({}).limit(100))
            data =convert_bson_types(data)
            return data

