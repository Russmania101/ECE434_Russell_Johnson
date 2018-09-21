// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include <unistd.h>
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio0_addr, *gpio1_addr;
    volatile unsigned int *gpio0_oe_addr, *gpio1_oe_addr;
    volatile unsigned int *gpio0_datain, *gpio1_datain;
    volatile unsigned int *gpio0_setdataout_addr, *gpio1_setdataout_addr;
    volatile unsigned int *gpio0_cleardataout_addr, *gpio1_cleardataout_addr;
    unsigned int reg;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    // GPIO0
    printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, GPIO0_SIZE);
    gpio0_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);

    gpio0_oe_addr           = gpio0_addr + GPIO_OE;
    gpio0_datain            = gpio0_addr + GPIO_DATAIN;
    gpio0_setdataout_addr   = gpio0_addr + GPIO_SETDATAOUT;
    gpio0_cleardataout_addr = gpio0_addr + GPIO_CLEARDATAOUT;

    if(gpio0_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO0 mapped to %p\n", gpio0_addr);
    printf("GPIO0 OE mapped to %p\n", gpio0_oe_addr);
    printf("GPIO0 SETDATAOUTADDR mapped to %p\n", gpio0_setdataout_addr);
    printf("GPIO0 CLEARDATAOUT mapped to %p\n", gpio0_cleardataout_addr);

    // GPIO1
    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);
    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio1_oe_addr           = gpio1_addr + GPIO_OE;
    gpio1_datain            = gpio1_addr + GPIO_DATAIN;
    gpio1_setdataout_addr   = gpio1_addr + GPIO_SETDATAOUT;
    gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEARDATAOUT;

    if(gpio1_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO1 mapped to %p\n", gpio1_addr);
    printf("GPIO1 OE mapped to %p\n", gpio1_oe_addr);
    printf("GPIO1 SETDATAOUTADDR mapped to %p\n", gpio1_setdataout_addr);
    printf("GPIO1 CLEARDATAOUT mapped to %p\n", gpio1_cleardataout_addr);

    // Set both LEDs to be outputs
    reg = *gpio1_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~GPIO1_16;       // Set GPIO1_16 bit to 0
    reg &= ~GPIO1_19;       // Set GPIO1_19 bit to 0
    *gpio1_oe_addr = reg;
    printf("GPIO1 configuration: %X\n", reg);

    printf("Start blinking LEDs on P9_15 & P9_16\n");
    while(keepgoing) {
        if (*gpio0_datain & GPIO0_30) 
        {
            *gpio1_setdataout_addr = GPIO1_16;
        }
        else
        {
            *gpio1_cleardataout_addr = GPIO1_16;
        }

        if (*gpio1_datain & GPIO1_17) 
        {
            *gpio1_setdataout_addr = GPIO1_19;
        }
        else
        {
            *gpio1_cleardataout_addr = GPIO1_19;
        }

	usleep(1);
    }

    munmap((void *)gpio1_addr, GPIO1_SIZE);
    munmap((void *)gpio0_addr, GPIO0_SIZE);
    close(fd);
    return 0;
}
