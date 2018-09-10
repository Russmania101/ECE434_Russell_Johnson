#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

pin = "P9_12"
GPIO.setup(pin, GPIO.OUT)
#delay = 0.05 # 100ms
#delay = 0.005 # 10ms
delay = 0.0005 # 1ms

while True:
    GPIO.output(pin, 1)
    time.sleep(delay)
    GPIO.output(pin, 0)
    time.sleep(delay)