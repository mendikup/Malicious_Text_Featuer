from pymongo import MongoClient
import os


class Dal:
    """Retrieve documents from a MongoDB collection."""

    def __init__(self):
        self.USER = os.getenv("USER", "IRGC_NEW")
        self.DB_NAME = os.getenv("DB_NAME", "IranMalDB")
        self.PASS = os.getenv("PASS", "iran135")
        self.COLLECTION = os.getenv("COLLECTION", "tweets")
        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")

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


    def get_data(self, counter, amount_per_pull = 100):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            raw_data = list(
                collection.find({})
                .sort("CreateDate")
                .skip(counter * amount_per_pull)
                .limit(amount_per_pull)
            )
            return raw_data

