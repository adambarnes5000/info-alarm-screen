import urllib2
import datetime

WUNDERGROUND_KEY = '61834b1832ab90d7'


def get_icon_url(icon):
    return "http://openweathermap.org/img/w/%s.png" % icon


def time_from_time_stamp(time_stamp):
    return datetime.datetime.fromtimestamp(time_stamp).strftime('%H:%M')


def get_weather():
    response = urllib2.urlopen(
        "http://api.wunderground.com/api/61834b1832ab90d7/geolookup/conditions/forecast/q/Ireland/Dublin.json")
    data = eval(response.read())
    return {
        "type": data['weather'][0]['main'],
        "description": data['weather'][0]["description"],
        "icon": get_icon_url(data['weather'][0]["icon"]),
        "temp": int(data['main']["temp"]),
        "pressure": data['main']["pressure"],
        "tempMin": int(data['main']["temp_min"]),
        "tempMax": int(data['main']["temp_max"]),
        "sunRise": time_from_time_stamp(data["sys"]["sunrise"]),
        "sunSet": time_from_time_stamp(data["sys"]["sunset"])
    }


if __name__ == "__main__":
    print get_weather()
