#!/usr/bin/python

from subprocess import Popen
import datetime
import random
import glob
import json

files = glob.glob('/home/pi/Alarms/*.mp3')

# TODO Bank Holidays

alarms = []


def load_alarms():
    global alarms
    alarms = json.load(open('/home/pi/Alarms/alarms.json'))


load_alarms()


def main():
    for alarm in alarms:
        if time_valid(alarm[0]) and day_valid(alarm[1]):
            play_file(random.choice(files))
        else:
            print 'Ignoring alarm %s %s' % alarm


def get_next_alarm():
    load_alarms()
    work_day_alarms = filter(lambda x: x[1] != 'WEEKEND', alarms)
    weekend_alarms = filter(lambda x: x[1] != 'WORKDAY', alarms)
    todays_alarms = work_day_alarms if is_work_day() else weekend_alarms
    tomorrows_alarms = work_day_alarms if is_tomorrow_work_day() else weekend_alarms
    todays_alarms = filter(lambda x: x[0] > get_time_now(), todays_alarms)
    if len(todays_alarms) > 0:
        return 'Today %s' % get_earliest_alarm_time(todays_alarms)
    if len(tomorrows_alarms) > 0:
        return 'Tomorrow %s' % get_earliest_alarm_time(tomorrows_alarms)
    return 'Monday %s' % get_earliest_alarm_time(alarms)


def get_earliest_alarm_time(alarms_list):
    return min(map(lambda x: x[0], alarms_list))


def time_valid(alarm_time):
    return alarm_time == get_time_now()


def get_time_now():
    return str(datetime.datetime.now().time().strftime('%H:%M'))


def day_valid(daytype):
    return daytype != 'WORKDAY' or is_work_day()


def is_work_day():
    day_no = int(datetime.datetime.now().date().strftime('%w'))
    return day_no in [1, 2, 3, 4, 5]


def is_tomorrow_work_day():
    day_no = int(datetime.datetime.now().date().strftime('%w'))
    return day_no in [0, 1, 2, 3, 4]


def play_file(music_file):
    print 'Playing file %s' % music_file
    Popen(['omxplayer', music_file])


if __name__ == "__main__":
    print get_next_alarm()
