#! /bin/bash

# config button
config-pin p9_24 gpio

# config LED
config-pin p9_15 gpio

# config ALERT for temp sensor
config-pin p9_41 gpio

# config LED matrix & temp sensors
config-pin p9_17 i2c
config-pin p9_18 i2c

# config rotary encoders
config-pin p8_33 qep
config-pin p8_35 qep
config-pin p8_41 qep
config-pin p8_42 qep