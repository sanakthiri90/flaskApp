import requests
from flask import Flask, jsonify, request
import json
import logging


logging.basicConfig(filename='./logs/app_log.log',
						filemode='a',
						format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
						datefmt='%H:%M:%S',
						level=logging.DEBUG)
app = Flask(__name__)


@app.route("/api/", methods=["POST"])
def hello():
	data = request.get_json()
	print(data)
	logging.info(data)
	return jsonify(data)


if __name__ == '__main__':
   app.run(debug=True, port=5052, host='0.0.0.0')

