from consumer import Consumer
from dal import Dal
import threading
import os


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.dal = Dal()

    def run(self):
        consume_topic_antisemitic = os.getenv("ROW_TWEETS_ANTISEMITIC", "enriched_preprocessed_tweets_antisemitic")
        consume_topic_not_antisemitic = os.getenv("ROW_TWEETS_NOT_ANTISEMITIC", "enriched_preprocessed_tweets_not_antisemitic")

        antisemitic_collection = os.getenv("###", "tweets_antisemitic")
        not_antisemitic_collection = os.getenv("@@@", "tweets_not_antisemitic")

        antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_antisemitic, antisemitic_collection), daemon=True)
        antisemitic.start()

        not_antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_not_antisemitic, not_antisemitic_collection), daemon=True)
        not_antisemitic.start()

    def start_listening(self, consume_topic, collection_to_save):
        print(f"Started listening to topic: {consume_topic}, inserting to {collection_to_save} collection.")

        self.dal.drop_table(collection_to_save)
        events = self.consumer.get_consumer_events(consume_topic)

        for event in events:
            processed_document = self.process_event(event)
            print(f"persister saving to collection: {collection_to_save}")
            print(processed_document)
            self.dal.insert_document(collection_to_save, processed_document)

    def process_event(self, event):
        processed_document = event.value
        return processed_document

