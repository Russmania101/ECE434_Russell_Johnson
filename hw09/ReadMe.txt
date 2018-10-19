Russell Johnson
ECE434
Homework 9

Project:
    - Griffin and I have switched from doing a bluetooth speaker to making a digital paperfootball 
    game board with automated scoring and a jumbotron.

PRU:
    - 2.6 - Blinking An LED - in "Blinking an LED" folder
        - Sample code blinks the USR3 LED just fine.
        - I modified the code to blink an LED on P9_27 and it works great
        - Screen capture showing me running the program is in "2.6.png"
            - How to run:
                - ./config_pin.sh 
                - source setup.sh 
                - make
        - Remove delays and hook up to scope
            - Scope capture is in "2.6_scope.png"
            - Toggle spped: 80ns
            - Jitter: lots of jitter
            - Stable: it is stable
    
    - 5.3 PWM Generator - all the following parts are in "PWM_Generator" folder
        - I took the sample code and changed the pin to P9_27, and the program runs great
        - Screen capture deomnstrating how I ran it is in "5.3.png"
        -   How to run:
            - ./config_pins.sh
            - source pwm1_setup.sh 
            - make
        - Connect to scope  
            - Scope capture is in "5.3_scope.png"
            - Stable: it isstable
            - Period: 15ns
            - Std Dev: 82ps std dev for the period
            - Jitter: no jitter
    
    - 5.4 Controlling the PWM Frequency
        - Sample code runs great
        - Screen capture is in "5.4.png"
            - How to run:
                - source pwm4_setup.sh
                - make
        - Connect to a scope
            - Scope capture for 2 of the PWM channels (P8_43 & P8_44) is in "5.4_scope.png"
            - Highest Frequency: 327kHz
            - Period: 3.06us
            - Jitter: veyr jittery
    
    - 5.5 Loop Unrolling
        - Sample code runs great
        - Screen Capture is in "5.5.png"
            - How to run:
                - source pwm5_setup.sh
                - make
        - Connect to a scope
            - Scope capture for 2 of the PWM channels (P8_45 & P8_46) is in "5.5_scope.png"
            - Period: 595ns
            - this is much faster than without loop unrolling (6 times ish)

    - 5.9 Reading an input at regular intervals
        - ran the sample code with the led on P9_27 and a button on p9_25 - works great
            - screen capture is in "5.9.png"
            - How to run:
                - source input_setup.sh
                - make
        - connect to a function generator and scope
            - scope capture is in "5.9_scope.png"
            - There is a 59.5ns delay between the input and output

    

