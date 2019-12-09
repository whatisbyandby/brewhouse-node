from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
producer = KafkaProducer(bootstrap_servers='192.168.0.28:9092')

# Asynchronous by default

if __name__ == '__main__':
    print(producer.bootstrap_connected())
    producer.send('simple_test', key='', value=b'trying again')
    producer.flush(15)
    print('Loop')

