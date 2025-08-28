from consumer import Consumer
from producer import Producer
from cleaner import Cleaner
from text_processor import TextProcessor
import threading
import os


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.producer = Producer()

    def run(self):
        consume_topic_antisemitic = os.getenv("ROW_TWEETS_ANTISEMITIC", "raw_tweets_antisemitic")
        consume_topic_not_antisemitic = os.getenv("ROW_TWEETS_NOT_ANTISEMITIC", "raw_tweets_not_antisemitic")

        publish_topic_antisemitic = os.getenv("preprocessed_tweets_antisemitic", "preprocessed_tweets_antisemitic")
        publish_topic_not_antisemitic = os.getenv("preprocessed_tweets_not_antisemitic", "preprocessed_tweets_not_antisemitic")

        antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_antisemitic, publish_topic_antisemitic), daemon=True)
        antisemitic.start()

        not_antisemitic = threading.Thread(target=self.start_listening, args=(consume_topic_not_antisemitic, publish_topic_not_antisemitic), daemon=True)
        not_antisemitic.start()

    def start_listening(self, consume_topic, publish_topic):
        print(f"Started listening to topic: {consume_topic}, publishing to: {publish_topic}.")
        events = self.consumer.get_consumer_events(consume_topic)

        for event in events:
            processed_document = self.process_event(event)
            print(f"preprocessor publishing to topic: {publish_topic}")
            print(processed_document)
            self.producer.publish_event(publish_topic, processed_document)

    def process_event(self, event):
        doc = event.value
        doc["original_text"] = doc.pop("text")

        cleaner = Cleaner(doc['original_text'])
        cleaner.remove_punctuation_and_special_characters()
        cleaner.remove_white_spaces()
        cleaned_text = cleaner.get_data()

        txt_processor = TextProcessor(cleaned_text)
        txt_processor.remove_stop_words()
        txt_processor.lower_words()
        txt_processor.lemmatize_words()
        processed_txt = txt_processor.get_data()

        doc['clean_text'] = processed_txt
        return doc

