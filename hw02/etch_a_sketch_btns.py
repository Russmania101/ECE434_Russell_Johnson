#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
from threading import Thread
import smbus
import time

bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

# button states
move_up = 0
move_down = 0
move_left = 0
move_right = 0
clear = 0

# button pins
btn_up = "P9_11"
btn_down = "P9_23"
btn_left = "P9_13"
btn_right = "P9_14"
btn_clear = "P9_24"

column = {1:0x00, 2:0x02, 3:0x04, 4:0x06, 5:0x08, 6:0x0A, 7:0x0C, 8:0x0E}
row = {1:0b10000000, 2:0b01000000, 3:0b00100000, 4:0b00010000, 5:0b00001000, 6:0b00000100, 7:0b00000010, 8:0b00000001}
clear_led = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
display = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

def handleUp(channel):
    global move_up

    #print("channel = " + channel)
    state = GPIO.input(channel)
    
    move_up = state

def handleDown(channel):
    global move_down

    #print("channel = " + channel)
    state = GPIO.input(channel)

    move_down = state

def handleLeft(channel):
    global move_left

    #print("channel = " + channel)
    state = GPIO.input(channel)
    
    move_left = state

def handleRight(channel):
    global move_right

    #print("channel = " + channel)
    state = GPIO.input(channel)
    
    move_right = state

def handleClear(channel):
    global clear

    #print("channel = " + channel)
    state = GPIO.input(channel)

    clear = state

def main():
    global btn_up, btn_down, btn_left, btn_right, btn_clear, bus, matrix, column, row
    global move_up, move_down, move_left, move_right, clear, display

    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

    # set the button GPIO pins as inputs
    GPIO.setup(btn_up, GPIO.IN)
    GPIO.setup(btn_down, GPIO.IN)
    GPIO.setup(btn_left, GPIO.IN)
    GPIO.setup(btn_right, GPIO.IN)
    GPIO.setup(btn_clear, GPIO.IN)

    # add detection event for each button: Rising, Falling, or Both
    GPIO.add_event_detect(btn_up, GPIO.BOTH, callback=handleUp)
    GPIO.add_event_detect(btn_down, GPIO.BOTH, callback=handleDown)
    GPIO.add_event_detect(btn_left, GPIO.BOTH, callback=handleLeft)
    GPIO.add_event_detect(btn_right, GPIO.BOTH, callback=handleRight)
    GPIO.add_event_detect(btn_clear, GPIO.BOTH, callback=handleClear)

    # print out instructions
    print ("\nInstructions: ")
    print ("Use the first four buttons to move up, down, left, and right on the LED matrix")
    print ("Use the last button to clear the LED matrix")

    # clear led matrix
    display = clear_led[:]
    bus.write_i2c_block_data(matrix, 0, display)

    # display initial dot on led matrix
    x = 4
    y = 4
    display[column[x]] = row[y]
    bus.write_i2c_block_data(matrix, 0, display)

    print ("\nRunning...")

    try:
        while True:
            # move cursor
            if move_up == 1:
                if y > 1:
                    y -= 1
                move_up = 0
            if move_down == 1:
                if y < 8:
                    y += 1
                move_down = 0
            if move_left == 1:
                if x > 1:
                    x -= 1
                move_left = 0
            if move_right == 1:
                if x < 8:
                    x += 1
                move_right = 0
            if clear == 1:
                display = clear_led[:]
                bus.write_i2c_block_data(matrix, 0, display)
                clear = 0

            # update LED matrix
            display[column[x]] = display[column[x]] | row[y]
            bus.write_i2c_block_data(matrix, 0, display)

    except KeyboardInterrupt:
        print ("\nCleaning Up...")
        GPIO.cleanup()
    GPIO.cleanup()

main()