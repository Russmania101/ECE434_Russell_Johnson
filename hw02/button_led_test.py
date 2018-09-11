#!/usr/bin/env python3

# Russell Johnson
# ECE434
# Homework 2

import Adafruit_BBIO.GPIO as GPIO
import time

# set button pins
btn1 = "P9_11"
btn2 = "P9_23"
btn3 = "P9_13"
btn4 = "P9_14"

# set LED pins
LED1 = "P9_15"
LED2 = "P9_16"
LED3 = "P9_19"
LED4 = "P9_20"

# set the LED GPIO pins as outputs
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

# set the button GPIO pins as inputs
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(btn3, GPIO.IN)
GPIO.setup(btn4, GPIO.IN)

# turn all LEDs off
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)

# map buttons to LEDs
map = {btn1 : LED1, btn2: LED2, btn3 : LED3, btn4 : LED4}

# Turn on/off LED if button is pressed
def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")

print("Running...")

# add detection event for each button: Rising, Falling, or Both
GPIO.add_event_detect(btn1, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(btn2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(btn3, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(btn4, GPIO.BOTH, callback=updateLED)

try:
    while True:
        time.sleep(100) # let other processes run
except KeyboardInterrupt:
    print("Cleaning Up...")
    GPIO.cleanup()
GPIO.cleanup()
