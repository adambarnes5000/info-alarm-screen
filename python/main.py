#!/usr/bin/python

from flask import Flask
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


@app.route("/news")
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


@app.route("/alarm")
@cross_origin()
def get_next_alarm():
    return alarms.get_next_alarm()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

app = Flask(__name__)
