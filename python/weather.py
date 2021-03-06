import urllib2
import datetime

SHORT_DESC_LEN = 60

def get_icon_url(icon):
    return "http://openweathermap.org/img/w/%s.png" % icon


def time_from_time_stamp(time_stamp):
    return datetime.datetime.fromtimestamp(time_stamp).strftime('%H:%M')


def get_weather():
    response = urllib2.urlopen(
        "http://api.wunderground.com/api/61834b1832ab90d7/geolookup/conditions/forecast/q/Ireland/Dublin.json")
    response_astro = urllib2.urlopen(
        "http://api.wunderground.com/api/61834b1832ab90d7/astronomy/q/Ireland/Dublin.json")
    data = eval(response.read())
    data_astro = eval(response_astro.read())
    sunrise=xpath_get(data_astro,'sun_phase/sunrise')
    sunset = xpath_get(data_astro, 'sun_phase/sunset')
    return {
        "current": get_current_weather(data),
        "forecast_day": get_forecast(xpath_get(data,'forecast/txt_forecast/forecastday')[0]),
        "forecast_night": get_forecast(xpath_get(data,'forecast/txt_forecast/forecastday')[1]),
        "moon": xpath_get(data_astro,'moon_phase/phaseofMoon'),
        "sunrise": '%s:%s' % (sunrise['hour'].zfill(2),sunrise['minute']),
        "sunset": '%s:%s' % (sunset['hour'].zfill(2), sunset['minute']),

    }


def get_current_weather(data):
    return {
        'icon_url': xpath_get(data,'current_observation/icon_url'),
        'temp': xpath_get(data, 'current_observation/temp_c'),
        'desc': xpath_get(data, 'current_observation/weather'),
    }


def get_forecast(data):
    return {
        'icon_url': xpath_get(data,'icon_url'),
        'desc': xpath_get(data, 'fcttext_metric'),
        'desc_short': get_short_desc(xpath_get(data, 'fcttext_metric')),
        'title': xpath_get(data, 'title'),
    }


def get_short_desc(desc):
    sentences = desc.split('. ')
    short_desc = ''
    if len(sentences[0]) > SHORT_DESC_LEN:
        return desc[:SHORT_DESC_LEN]+'...'
    for sentence in sentences:
        if (len(short_desc + sentence)) > SHORT_DESC_LEN:
            return short_desc[:-1] + '*'
        short_desc = '%s%s. ' % (short_desc, sentence)
    return desc


def xpath_get(mydict, path):
    elem = mydict
    # noinspection PyBroadException
    try:
        for x in path.strip("/").split("/"):
            try:
                x = int(x)
                elem = elem[x]
            except ValueError:
                elem = elem.get(x)
    except:
        pass

    return elem

if __name__ == "__main__":
    print get_short_desc("Showers early, then partly cloudy overnight. Low 6C. Winds WSW at 15 to 25 km/h. Chance of rain 70%.")
