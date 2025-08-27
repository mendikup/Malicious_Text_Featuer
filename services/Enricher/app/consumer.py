from kafka import KafkaConsumer
import json
import os


class Consumer:
    @staticmethod
    def get_consumer_events(topic):
        """return an object with all the last events waiting in the kafka server for the specified topic"""
        bootstrap_server = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
        return KafkaConsumer(topic,
                                         group_id='enricher-group',
                                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                         bootstrap_servers=[bootstrap_server]
                                      )