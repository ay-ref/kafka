import time
from confluent_kafka import Producer
import json

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


# Kafka configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9094',  # Replace with your Kafka broker address
}

producer = Producer(kafka_config)

topic = 'raw'

for i in range(20):
    message_data = {
                'id': i,
                'timestamp': int(time.time()),
                'message': f'Message {i}'
            }
    message_value = json.dumps(message_data)
    producer.produce(topic, value=message_value, callback=delivery_report)
    producer.poll(0)

producer.flush()
print("All messages sent successfully!")
