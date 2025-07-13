import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

message = {
    'to': 'recipient@example.com',
    'subject': 'Hello!',
    'body': 'This is a test email from RabbitMQ project.'
}

channel.basic_publish(
    exchange='',
    routing_key='email_queue',
    body=json.dumps(message)
)

print(" [x] Sent email task")

connection.close()
