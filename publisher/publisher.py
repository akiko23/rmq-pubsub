import os
import time

import pika
from pika.exchange_type import ExchangeType

EXCHANGE_NAME = 'file_data'
QUEUE_NAME = 'input_txt_lines'

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=os.getenv('RABBITMQ_HOST'),
    port=os.getenv('RABBITMQ_PORT'),
    credentials=pika.PlainCredentials(username=os.getenv('RABBITMQ_USER'), password=os.getenv('RABBITMQ_PASSWORD')),
))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=ExchangeType.direct)
channel.queue_declare(queue=QUEUE_NAME)
channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME)

try:
    with open('input.txt', 'r') as file:
        while True:
            for line in file:
                time.sleep(0.1)  # mocking long sending
                channel.basic_publish(exchange=EXCHANGE_NAME,
                                      routing_key=QUEUE_NAME,
                                      body=line)

            print('[p] Sent full file data. Wait for 2 seconds and iterate again')
            time.sleep(2)
            file.seek(0)
finally:
    channel.close()
    connection.close()
