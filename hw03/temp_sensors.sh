#! /bin/bash

# Russell Johnson
# ECE434
# Homework 3

# Temperature Sensors ADD0:
# GND -> 0x48
# V+ -> 0x4A
# Floating -> 0x49

while true
do
    # Read temp sensors on i2c bus 1
    temp1C = `i2cget -y 1 0x48` # ADD0 -> GND
    temp2C = `i2cget -y 1 0x4A` # ADD0 -> V+

    # Convert Celcius temps to fahrenheit
    temp1F = $(($temp1C * (9/5) + 32))
    temp2F = $(($temp2C * (9/5) + 32))

    # print out the temperatures
    echo Temperature 1: $temp1F degrees F
    echo Temperature 2: $temp2 degrees F

    # buffer time
    sleep 1
done