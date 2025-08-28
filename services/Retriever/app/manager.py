from dal import Dal
import time
import os
from producer import Producer
from utils_function import classify_antisemitic ,convert_bson_types


class Manager:

    def __init__(self):
        self.dal = Dal()
        self.producer = Producer()


    def run(self, interval = 10):
        publish_topic_antisemitic = os.getenv("preprocessed_tweets_antisemitic", "raw_tweets_antisemitic")
        publish_topic_not_antisemitic = os.getenv("preprocessed_tweets_not_antisemitic", "raw_tweets_not_antisemitic")
        print(f"publishing to {publish_topic_antisemitic}.")
        print(f"publishing to {publish_topic_not_antisemitic}.")

        counter = 0 # start counter to skip to prevent duplicate retrievals
        while True:
            print(f"new interval...")
            data = self.dal.get_data(counter, amount_per_pull=10)
            counter += 1
            print(f"fetched {len(data)} msgs.")
            antisemitic, not_antisemitic = classify_antisemitic(data)
            self.publish_tweets(publish_topic_antisemitic, antisemitic)
            self.publish_tweets(publish_topic_not_antisemitic, not_antisemitic)
            time.sleep(interval)

    def publish_tweets(self,topic, data):
        for document in data:
            document = convert_bson_types(document)
            print(f"retriever publishing to topic: {topic}")
            print(document)
            self.producer.publish_event(topic, document)