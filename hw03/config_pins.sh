#! /bin/bash

# config button
config-pin p9_24 gpio

# config LED matrix
config-pin p9_17 i2c
config-pin p9_18 i2c

# config rotary encoders
config-pin p8_33 qep
config-pin p8_35 qep
config-pin p8_41 qep
config-pin p8_42 qep