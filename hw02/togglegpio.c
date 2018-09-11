#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <libsoc_gpio.h>
#include <libsoc_debug.h>

/* Russell Johnson
 * ECE434
 * Homework 2
 */

// Blinks an LED attached to P9_14
#define GPIO_OUTPUT 60

//int delay = 50000; // 100ms
//int delay = 5000; // 10ms
//int delay = 500; // 1ms
int delay = 50; // 100us
//int delay = 5; // 10us
//int delay = 0.5; // 1us

int main(void) 
{
    gpio *gpio_output; // Create gpio pointer
    libsoc_set_debug(1); // Enable debug output
    // Request gpio
    gpio_output = libsoc_gpio_request(GPIO_OUTPUT,  LS_SHARED);
    // Set direction to OUTPUT
    libsoc_gpio_set_direction(gpio_output, OUTPUT);
    libsoc_set_debug(0);
    // Turn off debug printing
    // for fast toggle

    int i;
    for (i=0; i<1000000; i++) { // Toggle GPIO X times
        libsoc_gpio_set_level(gpio_output, HIGH);
        usleep(delay);
        
        libsoc_gpio_set_level(gpio_output, LOW);
        usleep(delay);
    }
    if (gpio_output) 
    {
        // Free gpio request memory
        libsoc_gpio_free(gpio_output); 
    }
    return EXIT_SUCCESS;
}
