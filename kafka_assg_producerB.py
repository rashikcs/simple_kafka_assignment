from time import sleep
from json import dumps
from kafka import KafkaProducer

from kafka import KafkaConsumer
from json import loads

def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
        
        

def main():
    print("python main function B")
    kafka_producer = connect_kafka_producer()
    for e in range(1, 10, 2):
        data = {'B' : e}
        #producer.send('numtest', value=data)
        publish_message(kafka_producer, "numtest", "B", str(e))
        sleep(2)
    
if __name__ == '__main__':
    main()