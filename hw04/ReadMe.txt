Russell Johnson
ECE434
Homework 4

Memory Map:
    - The memory map that I created for the BeagleBone Green Wireless is
      in the file bone_mmap.pdf

GPIO via mmap:
    1. Control two LEDs with 2 buttons using mmap - VERIFED WORKING
        - LED pins: p9_15 & p9_16
        - Button pins: p9_11 & p9_23
        - How to run:
            - ./config-pins.sh
            - make
            - sudo ./gpioToggle
        - Push the buttons to turn on their corresponding LEDs
    
    2. Toggle GPIO pin as fast as possible with mmap - VERIFIED WORKING
        - Tested with pin p9_15 at 10u and 1u
        - Compared to the table from hw2 - results in gpio_comp.pdf
        - run script:
            - ./config-pins.sh
            - make
            - sudo ./gpioToggleFast

    3. 





