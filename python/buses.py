import urllib2


def get_buses():
    return get_buses_for_stop(753, '39A') + get_buses_for_stop(781, '18')


def get_buses_for_stop(stop_id, route):
    response = urllib2.urlopen(
        "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=%s&format=json" % stop_id)
    data = eval(response.read())
    results = map(convert_entry, data['results'])
    return [x for x in results if x['route'] == route]


def convert_entry(entry):
    return {'route': entry['route'], 'destination': entry['destination'], 'time': entry['departuredatetime'][-8:-3]}


if __name__ == "__main__":
    print get_buses()
