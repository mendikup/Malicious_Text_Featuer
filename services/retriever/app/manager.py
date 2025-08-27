from dal import Dal
import time
from producer import Producer
from utils_function import classify_antisemitic ,convert_bson_types
import json


class Manager:

    def __init__(self):
        self.dal = Dal()
        self.producer = Producer()


    def run(self, interval = 60):
        counter = 0 # start counter to skip to prevent duplicate retrievals
        while True:
            data = self.dal.get_data(counter)
            antisemitic, not_antisemitic = classify_antisemitic(data)
            counter += 100
            self.publish_tweets("raw_tweets_antisemitic", antisemitic)
            self.publish_tweets("raw_tweets_not_antisemitic", not_antisemitic)
            time.sleep(interval)

    def publish_tweets(self,topic, data):
        for document in data:
            document = convert_bson_types(document)
            self.producer.publish_event(topic, document)
            print(json.dumps(document, indent=4))


m = Manager()
m.run()