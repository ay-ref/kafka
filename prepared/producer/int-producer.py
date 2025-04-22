import time
import csv
import json

from kafka import KafkaProducer

import config

producer = KafkaProducer(
    bootstrap_servers=config.sink_kafka_host,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

counter = 0

def produce_messages():
    global counter
    producer.send(config.sink_topic_name, value=counter)
    counter += 1
    producer.flush()
    print("All messages sent successfully!")

for i in range(100):
    produce_messages()
