#!/usr/bin/env python3

# From: https://adafruit-beaglebone-io-
# python.readthedocs.io/en/latest/Encoder.html

# Russell Johnson
# ECE434
# Homework 3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2
import time

# Instantiate the class to access channel eQEP2, and initialize
# that channel
myEncoder = RotaryEncoder(eQEP2)
myEncoder.setAbsolute()
myEncoder.enable()

# Get the current position
while True:
    print(myEncoder.position)
    time.sleep(0.1)
