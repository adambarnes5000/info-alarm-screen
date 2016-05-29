#!/usr/bin/python

from flask import Flask
from flask import request
from flask.ext.cors import CORS, cross_origin
import json

import news
import weather
import buses
import alarms
import commands

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/news", methods=['GET'])
@cross_origin()
def get_news():
    return str(json.dumps(news.get_news()))


@app.route("/weather")
@cross_origin()
def get_weather():
    return str(json.dumps(weather.get_weather()))


@app.route("/buses")
@cross_origin()
def get_buses():
    return str(json.dumps(buses.get_buses()))


@app.route("/killchromium")
@cross_origin()
def kill_chromium():
    commands.kill_chromium()
    return "Done"


@app.route("/nextalarm")
@cross_origin()
def get_next_alarm():
    return alarms.get_next_alarm()


@app.route("/alarms", methods=['GET'])
@cross_origin()
def get_alarms():
    return str(json.dumps(alarms.get_alarms()))

@app.route("/alarms", methods=['POST'])
@cross_origin()
def save_alarms():
    alarms.save(eval(request.data))
    return "Done"

@app.route("/holidays", methods=['GET'])
@cross_origin()
def get_holidays():
    return str(json.dumps(alarms.get_holidays()))

@app.route("/holidays", methods=['POST'])
@cross_origin()
def save_holidays():
    alarms.save_holidays(eval(request.data))
    return "Done"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

app = Flask(__name__)
