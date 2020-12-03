from flask import Flask
import pika

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>ok<h1>"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

if __name__ == "__main__":
    app.run()