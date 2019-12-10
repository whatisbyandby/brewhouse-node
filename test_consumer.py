from kafka import KafkaConsumer
import json
# To consume latest messages and auto-commit offsets
def consume():
    consumer = KafkaConsumer('fermentation',
        bootstrap_servers=['192.168.0.28:9092'])
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        message.offset, message.key,
        json.loads(message.value.decode('utf-8'))))


if __name__ == '__main__':
    consume()
