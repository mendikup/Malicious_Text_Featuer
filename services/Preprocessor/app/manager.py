from consumer import Consumer
import threading
import os


class Manager:
    def __init__(self):
        self.consumer = Consumer()

    def start_listening(self, topic):
        events = self.consumer.get_consumer_events(topic)

        for event in events:
            print("new massage:")
            print(f"topic: {event.topic}")
            print(event)

    def run(self):
        topic_raw_tweets_antisemitic = os.getenv("ROW_TWEETS_ANTISEMITIC", "raw_tweets_antisemitic")
        raw_tweets_not_antisemitic = os.getenv("ROW_TWEETS_NOT_ANTISEMITIC", "raw_tweets_not_antisemitic")

        antisemitic = threading.Thread(target=self.start_listening, args=(topic_raw_tweets_antisemitic,), daemon=True)
        antisemitic.start()

        not_antisemitic = threading.Thread(target=self.start_listening, args=(raw_tweets_not_antisemitic,), daemon=True)
        not_antisemitic.start()

