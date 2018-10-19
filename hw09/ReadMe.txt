Russell Johnson
ECE434
Homework 9

Project:
    - Griffin and I have switched from doing a bluetooth speaker to making a digital paperfootball 
    game board with automated scoring and a jumbotron.

PRU:
    - 2.6 - Blinking An LED
        - Sample code blinks the USR3 LED just fine.
        - I modified the code to blink an LED on P9_27 and it works great
        - Screen capture showing me running the program is in "2.6.png"
            - How to run:
                - ./config_pin.sh 
                - source setup.sh 
                - make
        - Remove delays and hook up to scope
            - Scope capture is in ""
            - Toggle spped: 
            - Jitter: 
            - Stable: 
    
    - 5.3 PWM Generator
        - I took the sample code and changed the pin to P9_27, and the program runs great
        - Screen capture deomnstrating how I ran it is in "5.3.png"
        -   How to run:
            - ./config_pins.sh
            - source pwm1_setup.sh 
            - make
        - Connect to scope  
            - Scope capture is in ""
            - Stable: 
            - Std Dev: 
            - Jitter: 
    
    - 5.4 Controlling the PWM Frequency
        - Sample code runs great
        - Screen capture is in "5.4.png"
            - How to run:
                - source pwm4_setup.sh
                - make
                - gcc pwm-test.c -o pwm-test
                - sudo ./pwm-test
        - Connect to a scope
            - Highest Frequency: 
            - Jitter: 