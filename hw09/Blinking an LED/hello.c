#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

#define GPIO1 0x4804C000
#define GPIO3 0x481AE000
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define USR0 (1<<21)
#define USR1 (1<<22)
#define USR2 (1<<23)
#define USR3 (1<<24)
#define P9_27 (1<<19) // GPIO3_19
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

//uint32_t gpio = 0x1<<5;

void main(void) {
	int i;

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1){
	//for(i=0; i<5; i++) {
		*GPIO3_SET = P9_27;      	// Turn on the LED on p9_27
		//__R30 |= gpio;
		__delay_cycles(0); //(500000000/5);    // Wait 1/2 second

		*GPIO3_CLEAR = P9_27;
		//__R30 &= ~gpio; 
		__delay_cycles(0); //(500000000/5); 
	}
	__halt();
}
