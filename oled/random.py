#!/usr/bin/python

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import random

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

# Draw a black filled box to clear the image.
while True:
    for x in range(127):
        for y in range(63):
            if random.choice([0,1]) == 1:
                draw.point((x,y),fill=255)
            else:
                draw.point((x, y), fill=0)
    disp.image(image)
    disp.display()

