from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os

class Dal:
    def __init__(self):
        """
        initialize with the database name from env variable
        and the name of the collection to work with
        """
        self.db = None
        self.database = os.getenv("MONGO_DB", "mydb")

    def insert_document(self, collection_name, document) -> dict:
        """
        insert a new document into the collection
        :param collection_name:
        :param document: the last consumption
        :return: an indication mag if inserted successfully
        """
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        with MongoClient(uri) as client:
            self.db = client[self.database]
            collection = self.db[collection_name]
            try:
                result = collection.insert_one(document)
                if result.inserted_id:
                    print(f"document id: {result.inserted_id} inserted.")
            except DuplicateKeyError as e:
                print(f"error: {e}")
            #     return {"msg": f"inserted successfully. _id: {result.inserted_id}"}
            # return {"msg": "there is is a problem inserting the data"}

    def drop_table(self, name):
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        with MongoClient(uri) as client:
            self.db = client[self.database]
            if name in self.db.list_collection_names():
                try:
                    result = self.db.drop_collection(name)
                    if result.get("ok", 0) == 1:
                        print(f"the collection {name} has been deleted.")
                except Exception as e:
                    print(e)
            print(f"the collection {name} is not in the database.")


