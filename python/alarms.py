#!/usr/bin/python

from subprocess import Popen
import datetime
import random
import glob
import json

files = glob.glob('/home/pi/Alarms/*.mp3')


def get_alarms():
    with open('/home/pi/Alarms/alarms.json') as f:
        alarms = json.load(f)
    return alarms


def get_holidays():
    with open('/home/pi/Alarms/holidays.json') as f:
        holidays = json.load(f)
    return holidays


def main():
    for alarm in get_alarms():
        if time_valid(alarm[0]) and day_valid(alarm[1]):
            play_file(random.choice(files))
        else:
            print 'Ignoring alarm %s ' % alarm


def get_next_alarm():
    alarms = get_alarms()
    work_day_alarms = filter(lambda x: x[1] != 'WEEKEND', alarms)
    weekend_alarms = filter(lambda x: x[1] != 'WORKDAY', alarms)
    todays_alarms = work_day_alarms if is_work_day() else weekend_alarms
    if len(todays_alarms) > 0:
        return 'Today %s' % get_earliest_alarm_time(todays_alarms)
    return find_next_alarm(work_day_alarms, weekend_alarms)


def find_next_alarm(work_day_alarms, weekend_alarms):
    for i in range(1,30):
        alarms = work_day_alarms if is_work_day(i) else weekend_alarms
        if len(alarms)>0:
            return '%s %s' % ({1:'Tomorrow'}.get(i,get_day_name(i)), get_earliest_alarm_time(alarms) )
    return '-'


def save(alarms):
    with open('/home/pi/Alarms/alarms.json', 'w') as outfile:
        json.dump(alarms, outfile)


def save_holidays(holidays):
    with open('/home/pi/Alarms/holidays.json', 'w') as outfile:
        json.dump(holidays, outfile)


def get_earliest_alarm_time(alarms_list):
    return min(map(lambda x: x[0], alarms_list))


def time_valid(alarm_time):
    return alarm_time == get_time_now()


def get_time_now():
    return str(datetime.datetime.now().time().strftime('%H:%M'))


def day_valid(daytype):
    return daytype != 'WORKDAY' or is_work_day()


def is_work_day(offset=0):
    day = (datetime.datetime.now()+datetime.timedelta(offset)).date()
    day_no = int(day.strftime('%w'))
    return day_no in [1, 2, 3, 4, 5] and not(day.strftime('%Y-%m-%d') in map(lambda x:x[0],get_holidays()))


def get_day_name(offset):
    day = (datetime.datetime.now()+datetime.timedelta(offset)).date()
    return day.strftime('%A')


def is_tomorrow_work_day():
    return is_work_day(1)


def play_file(music_file):
    print 'Playing file %s' % music_file
    Popen(['omxplayer', music_file])


if __name__ == "__main__":
    print get_next_alarm()
