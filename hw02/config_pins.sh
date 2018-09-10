#! /bin/bash

# config LEDs
config-pin p9_15 gpio
config-pin p9_16 gpio
config-pin p9_19 gpio
config-pin p9_20 gpio

# config buttons
config-pin p9_11 gpio
config-pin p9_23 gpio
config-pin p9_13 gpio
config-pin p9_14 gpio
config-pin p9_24 gpio

# config LED matrix
config-pin p9_17 i2c
config-pin p9_18 i2c