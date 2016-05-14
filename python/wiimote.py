#!/usr/bin/python

import glob
import random
from subprocess import Popen

import cwiid
import time

button_delay = 0.1

files = glob.glob('/home/pi/Alarms/*.mp3')


def play_file(music_file):
    Popen(['omxplayer', music_file])


print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
    quit()

print 'Wiimote connection established\n'
print 'Must be running as root to toggle display\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    # Detects whether + and - are held down and if they are it quits the program
    if buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0:
        print '\nClosing connection ...'
        # NOTE: This is how you RUMBLE the Wiimote
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)

    if buttons & cwiid.BTN_1:
        print 'Playing alarm'
        play_file(random.choice(files))
        time.sleep(button_delay)

    if buttons & cwiid.BTN_2:
        print 'Stopping alarm'
        Popen(['killomx'])
        time.sleep(button_delay)

    if buttons & cwiid.BTN_A:
        print 'Display off'
        Popen(['displayoff'])
        time.sleep(button_delay)

    if buttons & cwiid.BTN_B:
        print 'Display on'
        Popen(['displayon'])
        time.sleep(button_delay)
