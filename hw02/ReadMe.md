Russell Johnson
ECE434 Homework 2

- Button and LEDs
	1) Successfully wired up 4 buttons to the BeagleBone
		- Pins: P9_11, P9_23, P9_13, P9_14
	2. Successfully wired up 4 LEDs to the BeagleBone
		- Pins: P9_15, P9_16, P9_19, P9_20
	3. Wrote a python script that turns on an LED when its 
	   corresponding button is pressed
		- called button_led_test.py
		- run ./config_pins.sh
		- run ./button_led_test.py

- GPIO Pin on an Oscilloscpe
	- Bash Questions
		1. Min = 100mV, Max = 3.25V
		2. 4.2Hz -> 238ms
		3. 238ms - 100ms = 138ms
		4. OS handles when each program is executed, so you get what you get
		5. 4% CPU
		6. 1ms is about the shortest period I can get
			- table is in gpio_tables.docx
		7. The period is slightly unstable at 1ms
		8. The period is still slightly unstable at 1ms
		9. Cleaning up the file did not affect the period
		10. Period is still the same with sh instead of bash
		11. 1ms is still about the shortest period I can get
	 - Python Questions
	 	1. Min = 100mV, Max = 3.25V
		2. 100ms
		3. 0ms
		4. python is much faster than direct hardware access using bash/shell
		5. 3% CPU
		6. 1ms is about the shortest stable period I can get with a small difference in period
			- table is in gpio_tables.docx
		7. The period is stable at 1ms
		8. The period is still stable at 1ms
		9. N/A
		10. N/A
		11. 1ms is the shortest stable period that I can get
	- C Questions
		1. Min = 100mV, Max = 3.25V
		2. 100.5ms
		3. 100.5 - 100 = 0.5ms
		4. C is still much faster than direct hardware access using bash/shell, but the OS still plays a role
		5. 2.6%
		6. 1ms is about the shortest stable period I can get with a small difference in period
			- table is in gpio_tables.docx
		7. The period is stable at 1ms
		8. The period is still stable at 1ms
		9. N/A
		10. N/A
		11. 1ms is the shortest stable period that I can get

- Add buttons to Etch-A-Sketch python script
	- I added 5 buttons:
		1. Up - P9_11
		2. Down - P9_23
		3. Left - P9_13
		4. Right - P9_14
		5. Clear - P9_24
	- I also went ahead and added the LED Matrix
		- i2c bus 1: Data - P9_17, CLK - P9_18
	- How to run:
		1. ./config_pins.sh
		2. ./etch_a_sketch_btns.py
		3. Instructions will be printed out

