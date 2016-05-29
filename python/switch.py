#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime
from subprocess import Popen


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if not (GPIO.input(17)) and not(GPIO.input(18)):
        Popen(['killchromium'])
        time.sleep(5)
    if not(GPIO.input(17)):
        time_now = datetime.datetime.now().time().strftime('%I:%M %p').replace(':0',' o ')
        if time_now[0]=='0':
            time_now=time_now[1:]
        Popen(['say','The time is %s' % time_now])
        time.sleep(1)
    if not(GPIO.input(18)):
        Popen(['displaytoggle'])
        Popen(['killomx'])
        time.sleep(1)
