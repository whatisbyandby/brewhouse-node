from confluent_kafka import Producer

p = Producer({'bootstrap.servers': '192.168.0.28:9092'})


def produce():
    p.produce('simple_test', key='hello', value='world')
    p.flush(30)


if __name__ == '__main__':
    produce()