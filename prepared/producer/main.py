import time
import csv
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9094',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'aytopic'

def produce_messages(message="nothing"):
    producer.send(topic, value=message)
    print(f"sent: {message}")

    producer.flush()
    print("All messages sent successfully!")

while True:
    word = input("new word: ")
    produce_messages(word)
