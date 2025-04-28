import time
from confluent_kafka import Producer
import json
from random import randint
import random

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

kafka_config = {
    'bootstrap.servers': 'localhost:9094',
}

producer = Producer(kafka_config)

topic = 'strings'

ali_count = 3
abbas_count = 2

for i in range(ali_count):
    message_data = "ali"
    message_value = json.dumps(message_data)
    producer.produce(topic, value=message_value, callback=delivery_report)
    producer.poll(0)

for i in range(abbas_count):
    message_data = "abbas"
    message_value = json.dumps(message_data)
    producer.produce(topic, value=message_value, callback=delivery_report)
    producer.poll(0)

producer.flush()
print("All messages sent successfully!")
