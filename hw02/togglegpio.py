#!/usr/bin/env python3

# Russell Johnson
# ECE434
# Homework 2

import Adafruit_BBIO.GPIO as GPIO
import time

pin = "P9_12"
GPIO.setup(pin, GPIO.OUT)

#delay = 0.05 # 100ms
#delay = 0.005
#delay = 0.0005
delay = 0.00005 # 100us
#delay = 0.000005 # 10us

while True:
    GPIO.output(pin, 1)
    time.sleep(delay)
    GPIO.output(pin, 0)
    time.sleep(delay)
