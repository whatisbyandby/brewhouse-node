from kafka import KafkaConsumer
# To consume latest messages and auto-commit offsets
def consume():
    consumer = KafkaConsumer('simple_test',
        bootstrap_servers=['192.168.0.28:9092'])
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        message.offset, message.key,
        message.value))


if __name__ == '__main__':
    consume()
