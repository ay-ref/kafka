from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuration for the consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': '10',         # Consumer group id
    'auto.offset.reset': 'earliest'          # Start reading from the beginning if no offset is found
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'speed2'
consumer.subscribe([topic])

# Function to handle message consumption
def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll messages from Kafka
            if msg is None:  # No new message
                continue
            if msg.error():  # Check if there's an error
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        print("Consumption interrupted.")
    finally:
        # Close the consumer
        consumer.close()

# Start consuming messages
consume_messages()
