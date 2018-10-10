Russell Johnson
ECE434
Homework 6

Projects:
    - Griffin and I put are name next to our project idea (Bluetooth Speaker)
        - The beagle bone will be connected to a speaker inside of an enclosure that we will make
        - you can then connect your phone to the bone and play music from your phone, through the speakers

Watch:
    1. She works at National Instruments
    2. PREEMPT-RT is a Linux patch that turns it into a more accurate real-time OS by allowing the preemption of executing processes
    3. Real-time tasks and non time critical tasks running together (2 different degrees of time sensitivity)
         - Can have separate hardware devices for each tasks
    4. Driver stack are shared between the RT tasks and non-RT tasks
    5. Time it takes for an external event to occur until the relevant real-time task executes
    6. Take a time stap. sleep for fixed duration, take another time stamp, and then subtract the first time stamp 
       and the fixed duration from the second time stamp to get your delta.
    7. Delta is plotted in the histrogram. (latency samples)
    8. Dispatch latency - time between actual harware firing to the interrupt being woken up
       Scheduling latency - time it takes from the moment that the scheduler is aware of the task that needs to be run
       to when the task is actually scheudled on the CPU
    9. Mainline - Mainline kernels are built from the latest unmodified mainline Linux kernel sources
        - one of the main contributers is long-running interrupts. Implicitly executed with interrupts disabled because interrupt                        
       handlers are exectued in hard IRQ context.
    10. The low priority interrupt must finish executing before the external event can start
    11. Enabling the PREEMPT_RT patch allows you to force IRQ threads
        - little code executed in hard interrupt context
        - can allow premptive threads

========================
Professor Yoder's Comments

Score:  10/10