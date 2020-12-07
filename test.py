from flask import Flask
import pika

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>success<h1>'

print("----------")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.qeue_declare(queue='request')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
channel.close()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

if __name__ == "__main__":
    app.run()