Russell Johnson
ECE434 Homework 3

1. TMP101 Sensors
    - Hooked up both TMP101 Sensors to i2c bus 1
        - SCL - p9_17
        - Data - p9_18
        - ADD0 - first sensor: GND, second sensor: V+
    - Wrote a bash script to read the temperature values of both sensors
        - How to run:
            - ./config_pins.sh
            - ./temp_sensors.sh

2. Etch-a-Sketch
    - LED Matrix was added in HW2
        - i2c bus 1: Data - P9_17, CLK - P9_18
    - Clear button was added in HW2
        - P9_24
    - 2 rotary encoders added
        - Vertical: eQEP2 - p8_41 (A_IN), p8_42 (B_IN)
        - Horizontal: eQEP1 - p8_35 (A_IN), p8_33 (B_IN)
    - How to run:
        - ./config_pins.sh
        - ./etch_a_sketch_rotary_led.py
        - Instructions will be printed out

3. Extras
    - Added a temperature sensor and LED to the etch-a-sketch program
        - Temp sensor:
            - SCL - p9_17
            - Data - p9_18
            - ADD0 - GND
            - ALERT - p9_41
        - LED:
            - p9_15
        - When the temperature sensor reaches 30 degrees celcius, the LED lights
          up, and the LED matrix is cleared