from flask import Flask
import pika

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>success<h1>'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.qeue_declare(queue='request')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
channel.close()

if __name__ == "__main__":
    app.run()