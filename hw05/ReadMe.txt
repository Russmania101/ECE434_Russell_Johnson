Russell Johnson
ECE434
Homework 5

- Project
    - Griffin and I added a project idea (bluetooth speaker) to the Project Google Doc

- Make
    - Part A:
        - Target = app.o
        - Dependency = app.c
        - Command = gcc
        - -c = compile or assmeble souce files, but do not link
        - Makefile has been created and verified working
    - Part B 
        - Updated Makefile
            - added built-in and user-defined variables
            - Verified working correctly

- Installing the Kernel Source
    - Version 4.9 has been installed on host & bone

- Cross-Compiling
    - Image of helloWorld running on host is in hello_world_host.png
    - Image of helloWorld running on bone is in hellow_world_bone.png

- Kernel Modules
    - Part 1:
        - Installed everything that was needed successfuly
        - Verified that the hello.ko file runs properly
        - The file "Part 1-1.PNG" shows the first part of part 1 running
        - The file "Part 1-2.PNG" shows the second part (paramters) of part 1 running
        - Relevant files are in the hello/ directory
    - Part 2:
        - Verified that ebbchar properly runs
        - The file "Part 2.PNG" shows this program running properly
        - Relevant files are in the ebbchar/ directory
    - Part 3
        - Added a button to P9_15 and an led to P9_16
        - modified gpio_test.c to work with those 2 pins
        - verified that the program works correctly
        - output from the kernel log can be seen in "Part 3 - kernel log.PNG"
        - Relevant files are in the gpio_test/ directory

========================
Professor Yoder's Comments

Looks good. You Makefile doesn't look updated.

Score:  10/10