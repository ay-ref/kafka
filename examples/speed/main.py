import time
from confluent_kafka import Producer
import json
from random import randint
from uuid import uuid4

def create_random_speed_json():
    uid = uuid4()
    speed = randint(10, 20)
    angle = randint(0, 359)
    
    json_dict_data = {
                'id': str(uid),
                'timestamp': int(time.time()),
                'speed': speed,
                'angle': angle,
            }

    return json_dict_data
    

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


kafka_config = {
    'bootstrap.servers': 'localhost:9094',
}

producer = Producer(kafka_config)

topic = 'speed'
test_count = 20

for i in range(test_count):
    message_data = create_random_speed_json()
    message_value = json.dumps(message_data)
    producer.produce(topic, value=message_value, callback=delivery_report)
    producer.poll(0)

producer.flush()
print("All messages sent successfully!")
