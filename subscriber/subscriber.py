import os
import time

import pika
from pika.adapters.blocking_connection import BlockingChannel

from db import Database

EXCHANGE_NAME = 'file_data'
QUEUE_NAME = 'input_txt_lines'


def init_rabbitmq_client():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.getenv('RABBITMQ_HOST'),
        port=os.getenv('RABBITMQ_PORT'),
        credentials=pika.PlainCredentials(username=os.getenv('RABBITMQ_USER'), password=os.getenv('RABBITMQ_PASSWORD')),
    ))
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')
    channel.queue_declare(queue=QUEUE_NAME)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME)

    return channel


def callback(ch: BlockingChannel, method, properties, body):
    # mocking hard cpu bound task
    time.sleep(0.2)
    print(f" [c] {body}")
    db.add_message(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


db = Database(
    msg_table_name=os.getenv("MESSAGE_TABLE"),
    cassandra_host=os.getenv('CASSANDRA_HOST')
)

rmq_channel = init_rabbitmq_client()
rmq_channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=callback)

print("[*] Waiting for messages. To exit press CTRL+C")
rmq_channel.start_consuming()
