#!/usr/bin/python

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import random
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
i=0
while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    for x in range(127):
        y = 32+math.sin(math.pi/128*6*(x+i))*24
        draw.point((x, y), fill=255)
    i+=5
    disp.image(image)
    disp.display()

