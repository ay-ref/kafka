from confluent_kafka import Consumer, KafkaError
import json

def multiple_topic_polling():    
    config = {
        'bootstrap.servers': 'localhost:9094',
        'group.id': 'mygroupid',
        'auto.offset.reset': 'earliest',
        # 'enable.auto.commit': False,  # More control
    }
    
    consumer = Consumer(config)
    consumer.subscribe(['speed1', 'speed2'])
    
    try:
        while True:
            msg = consumer.poll(1.0)  # Timeout in seconds
            
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break
            
            # Message processing
            print(f"Topic: {msg.topic()}, Partition: {msg.partition()}")
            value = json.loads(msg.value().decode('utf-8')) if msg.value() else None
            print(value)
            
            # Manual offset commit for better control
            # consumer.commit(message=msg, asynchronous=False)
            
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        consumer.close()

multiple_topic_polling()