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
            - ./install.sh
            - ./config-pins.sh
            - make
            - sudo ./gpioToggle
        - Push the buttons to turn on their corresponding LEDs
    
    2. Toggle GPIO pin as fast as possible with mmap - VERIFIED WORKING
        - Tested with pin p9_15 at 10u and 1u
        - Compared to the table from hw2 - results in gpio_comp.pdf
        - run script:
            - install.sh
            - ./config-pins.sh
            - make
            - sudo ./gpioToggleFast

LCD Display
    - Plug in and Turn on - VERIFIED WORKING
        - I wired up the LCD as described on the wiki
        - The LCD properly turns on and runs

    - Display Images & Movie - VERIFIED WORKING
        - Display an image.
        - Display an image rotated 90 degrees.
        - Play a movie.
        - How to run:
            - ./install.sh
            - ./Display_Image.sh
            - ./off.sh

    - Display text on the LCD - VERIFIED WORKING
        - How to run:
            - ./install.sh
            - ./on.sh
            - ./text.sh
            - ./off.sh



