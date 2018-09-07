#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

# set button pins
btnUP = "P9_11"
btnDOWN = "P9_21"
btnLEFT = "P9_13"
btnRIGHT = "P9_14"

# set the button GPIO pins as inputs
GPIO.setup(btnUP, GPIO.IN)
GPIO.setup(btnDOWN, GPIO.IN)
GPIO.setup(btnLEFT, GPIO.IN)
GPIO.setup(btnRIGHT, GPIO.IN)

def moveUp(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    print("Up")
    #GPIO.output(map[channel], state)
    #print(map[channel] + " Toggled")

def moveDown(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    print("Down")
    #GPIO.output(map[channel], state)
    #print(map[channel] + " Toggled")

def moveLeft(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    print("Left")
    #GPIO.output(map[channel], state)
    #print(map[channel] + " Toggled")

def moveRight(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    print("Right")
    #GPIO.output(map[channel], state)
    #print(map[channel] + " Toggled")

print("Running...")

# add detection event for each button: Rising, Falling, or Both
GPIO.add_event_detect(btnUP, GPIO.BOTH, callback=moveUp)
GPIO.add_event_detect(btnDOWN, GPIO.BOTH, callback=moveDown)
GPIO.add_event_detect(btnLEFT, GPIO.BOTH, callback=moveLeft)
GPIO.add_event_detect(btnRIGHT, GPIO.BOTH, callback=moveRight)

# print out instructions
print ("\nInstructions: ")
print ("Use the four buttons to move up, down, left, and right and draw on the screen")

try:
    while True:
        time.sleep(100) # let other processes run
except KeyboardInterrupt:
    print("Cleaning Up...")
    GPIO.cleanup()
GPIO.cleanup()