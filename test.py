from flask import Flask,jsonify
import pika
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>success<h1>'

@app.route('/method',methods=['POST','GET'])
def getMtehod():
    response_list = {
        "url":request.url,
        "method":request.method
    }
    return jsonify(response_list)

if __name__ == "__main__":
    app.run()