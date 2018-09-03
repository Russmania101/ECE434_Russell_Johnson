#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)

def main():
    pygame.init()

    # get screen size from user
    screenWidth = input("Set screen pixel width: ")
    screenHeight = input("Set screen pixel height: ")

    # make sure screen size is valid
    if screenWidth < 100:
        screenWidth = 100
    elif screenWidth > 1000:
        screenWidth = 1000
    if screenHeight < 100:
        screenHeight = 100
    elif screenHeight > 1000:
        screenHeight= 1000

    # get initial (x,y) position from user
    x = input("Set initial x pixel position: ")
    y = input("Set initial y pixel position: ")

    # verify the given initial position is within the screen
    if x < 0:
        x = 0
    elif x > screenWidth:
        x = screenWidth
    if y < 0:
        y = 0
    elif y > screenHeight:
        y = screenHeight

    # set clock
    clock = pygame.time.Clock()

    # set screen size
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # clear screen
    screen.fill(white)

    while 1:
        # keep game at max 80 fps
        clock.tick(80)

        # draw the initial dot on the screen
        pygame.draw.circle(screen, black, (x,y), 2)
        pygame.display.update()

        # handle a key being pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] : x+=1
        if key[pygame.K_LEFT] : x-=1
        if key[pygame.K_UP] : y-=1
        if key[pygame.K_DOWN] : y+=1
        if key[pygame.K_q] : sys.exit()
        if key[pygame.K_c] : screen.fill(white)

        # handle special case for quit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

#main()

if __name__ == "__main__":
    main()