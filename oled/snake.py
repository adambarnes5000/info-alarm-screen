#!/usr/bin/python

import time
import sys

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import random
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

snake_length = int(sys.argv[1]) if len(sys.argv)>1 else 40
speed = int(sys.argv[2]) if len(sys.argv)>2 else 5

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

directions_map = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

snake = []
head = 0

direction = 1


def turn_snake():
    global direction
    direction = (direction + random.choice([-1,1])) % 4


def get_next_pos():
    return tuple(map(sum, zip(snake[head], directions_map[direction])))

def move_snake():
    global head
    tail_pos = snake[(head+1)%snake_length]
    head_pos = snake[head]
    draw.point(tail_pos, fill=0)
    tail_pos = tuple(map(sum, zip(head_pos, directions_map[direction])))
    tail_pos = (tail_pos[0] % 128, tail_pos[1] % 64)
    draw.point(tail_pos, fill=255)
    head = (head+1)%snake_length
    snake[head] = tail_pos


for i in range(snake_length):
    snake.append((10+i,50))
    draw.point(snake[i], fill=255)


draw.rectangle((0, 0, width, height), outline=0, fill=0)

while True:
    for i in range(speed):
        next_pos = get_next_pos()
        if next_pos in snake or 1 == random.randrange(0,12):
            turn_snake()
        move_snake()
    disp.image(image)
    disp.display()
