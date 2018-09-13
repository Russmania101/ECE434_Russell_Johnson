#!/usr/bin/env python3

# Russell Johnson
# ECE434
# Homework 3

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
from threading import Thread
import smbus
import time

# led matrix setup
bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# temperature sensor setup
temp = 0x48           # Use address 0x48
alarm = 30            # 30 degress Celcius

# clear button state
clear = 0

# button pins
btn_clear = "P9_24"

# ALRM pin for temp sensor 1
ALRM = "P9_41"

# set LED pin
LED = "P9_15"

# rotary encoders
rotary_vertical = RotaryEncoder(eQEP2)
rotary_horizontal = RotaryEncoder(eQEP1)

# encoder vars
step_size = 4 # each turn off encoder = +/-4

# led matrix vars
column = {1:0x00, 2:0x02, 3:0x04, 4:0x06, 5:0x08, 6:0x0A, 7:0x0C, 8:0x0E}
row = {1:0b10000000, 2:0b01000000, 3:0b00100000, 4:0b00010000, 5:0b00001000, 6:0b00000100, 7:0b00000010, 8:0b00000001}
clear_led = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
display = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

def handleClear(channel):
    global clear

    #print("channel = " + channel)
    state = GPIO.input(channel)

    clear = state

def main():
    global btn_clear, bus, matrix, column, row, step_size, ALRM, temp, alarm
    global clear, display, rotary_vertical, rotary_horizontal

    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

    # set the button GPIO pins as inputs
    GPIO.setup(btn_clear, GPIO.IN)

    # set the ALRM GPIO pin as input (for temp sensor 1)
    GPIO.setup(ALRM, GPIO.IN)

    # configure temperature sensor alarm
    bus.write_byte_data(temp, 1, 0x80)
    bus.write_byte_data(temp, 2, alarm) # Low alarm temp
    bus.write_byte_data(temp, 3, alarm) # High alarm temp

    # set the LED GPIO pin as outputs
    GPIO.setup(LED, GPIO.OUT)

    # turn LED off
    GPIO.output(LED, 0)

    # set up encoders
    rotary_vertical.setAbsolute()
    rotary_vertical.enable()
    rotary_horizontal.setAbsolute()
    rotary_horizontal.enable()

    # add detection event for clear button: Rising, Falling, or Both
    GPIO.add_event_detect(btn_clear, GPIO.BOTH, callback=handleClear)

    # print out instructions
    print ("\nInstructions: ")
    print ("\t1. Use the two rotary encoders to 'draw' on led matrix:")
    print ("\t\tfirst - up/down, second - left/right")
    print ("\t2. Use the button to clear the led matrix")
    print("\t3. If the temp sensor reaches 30 Celcius, the led matrix will clear")

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
        last_vertical_pos = rotary_vertical.position;
        last_horiz_pos = rotary_horizontal.position
        while True:
            
            # get rotary enconder positions
            vertical_pos = rotary_vertical.position
            horizontal_pos = rotary_horizontal.position

            # handle vertical movement
            if vertical_pos >= last_vertical_pos + step_size: # up
                if y < 8:
                    y += 1
                last_vertical_pos = vertical_pos
            elif vertical_pos <= last_vertical_pos - step_size: # down
                if y > 1:
                    y -= 1
                last_vertical_pos = vertical_pos

            # handle horizontal movement
            if horizontal_pos >= last_horiz_pos + step_size: # right
                if x > 1:
                    x -= 1
                last_horiz_pos = horizontal_pos
            elif horizontal_pos <= last_horiz_pos - step_size: # left
                if x < 8:
                    x += 1
                last_horiz_pos = horizontal_pos
            
            # clear led if clear button pressed
            if clear == 1:
                display = clear_led[:]
                bus.write_i2c_block_data(matrix, 0, display)
                clear = 0

            # check if temp alarm has been hit: clear and turn on LED if so
            if GPIO.input(ALRM) == 0:
                # Get temp
                tempC = bus.read_byte_data(temp, 0) # 0 = temperature
                tempF = (tempC * 9/5) + 32
                print("Temperature alarm triggered at %d degrees Fahrenheit" % (tempF))

                # Turn on LED
                GPIO.output(LED, 1)

                # Clear LCD
                display = clear_led[:]
                bus.write_i2c_block_data(matrix, 0, display)
            elif GPIO.input(ALRM) == 1:
                # Turn off LED
                GPIO.output(LED, 0)

            # update LED Matrix
            display[column[x]] = display[column[x]] | row[y]
            bus.write_i2c_block_data(matrix, 0, display)

    except KeyboardInterrupt:
        print ("\nCleaning Up...")
        GPIO.cleanup()
    GPIO.cleanup()

main()
