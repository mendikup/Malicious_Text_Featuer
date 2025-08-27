from consumer import Consumer
from producer import Producer
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
            print("new massage:")
            print(f"topic: {event.topic}")
            print(event)
            processed_event = self.process_event(event)
            self.producer.publish_event(publish_topic, processed_event)

    def process_event(self, event):
        processed_event = event.value
        return processed_event

