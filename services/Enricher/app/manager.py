from consumer import Consumer
from producer import Producer
from analyzer import Analyzer
import threading
import os


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.producer = Producer()

    def run(self):
        consume_topic_antisemitic = os.getenv("PREPROCESSED_TWEETS_ANTISEMITIC", "preprocessed_tweets_antisemitic")
        consume_topic_not_antisemitic = os.getenv("PREPROCESSED_TWEETS_NOT_ANTISEMITIC", "preprocessed_tweets_not_antisemitic")

        publish_topic_antisemitic = os.getenv("preprocessed_tweets_antisemitic", "enriched_preprocessed_tweets_antisemitic")
        publish_topic_not_antisemitic = os.getenv("preprocessed_tweets_not_antisemitic", "enriched_preprocessed_tweets_not_antisemitic")

        antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_antisemitic, publish_topic_antisemitic), daemon=True)
        antisemitic.start()

        not_antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_not_antisemitic, publish_topic_not_antisemitic), daemon=True)
        not_antisemitic.start()

    def start_listening(self, consume_topic, publish_topic):
        print(f"Started listening to topic: {consume_topic}, publishing to: {publish_topic}.")
        events = self.consumer.get_consumer_events(consume_topic)

        for event in events:
            processed_document = self.process_event(event)
            print(f"enricher publishing to topic: {publish_topic}")
            print(processed_document)
            self.producer.publish_event(publish_topic, processed_document)

    def process_event(self, event):
        doc = event.value
        original_text = doc['original_text']
        sentiment = Analyzer.find_sentiment(original_text)
        weapons_detected = Analyzer.detect_weapons(original_text)
        relevant_timestamp = Analyzer.find_relevant_timestamp(original_text)

        doc['sentiment'] = sentiment
        doc['weapons_detected'] = weapons_detected
        doc['relevant_timestamp'] = relevant_timestamp
        return doc

