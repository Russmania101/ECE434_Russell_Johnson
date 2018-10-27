#!/bin/bash

for i in {1..25}
do
	# Read temp sensor on i2c bus 1
	temp1C=`i2cget -y 1 0x48` # ADD0 -> GND

	# Convert Celcius temps to fahrenheit
	temp1F=$((($temp1C * 9/5) + 32))

	./demo.py $temp1F 0 

	sleep 1
done
