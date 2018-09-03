#!/usr/bin/env python

# Russell Johnson
# ECE434
# Homework 1

import pygame, sys
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
maxScreenLength = 800
minScreenLength = 100
minPosition = 0
positionBuffer = 100
fps = 80
dotSize = 4

def main():
    pygame.init()

    # get screen size from user
    screenWidth = input("Set screen pixel width: ")
    screenHeight = input("Set screen pixel height: ")

    # make sure screen size is valid
    if screenWidth < minScreenLength:
        screenWidth = minScreenLength
        print "Screen width is set to minimum of", minScreenLength
    elif screenWidth > maxScreenLength:
        screenWidth = maxScreenLength
        print "Screen width is set to maximum of", maxScreenLength
    if screenHeight < minScreenLength:
        screenHeight = minScreenLength
        print "Screen height is set to minimum of", minScreenLength
    elif screenHeight > maxScreenLength:
        screenHeight= maxScreenLength
        print "Screen height is set to maximum of", maxScreenLength

    # get initial (x,y) position from user
    x = input("Set initial x pixel position: ")
    y = input("Set initial y pixel position: ")

    # verify the given initial position is within the screen
    if x < minPosition:
        x = minPosition
        print "X cursor position is set to minimum of", minPosition
    elif x > screenWidth:
        x = screenWidth - positionBuffer
        print "X cursor position is set to maximum of", screenWidth - positionBuffer
    if y < minPosition:
        y = minPosition
        print "Y cursor position is set to minimum of", minPosition
    elif y > screenHeight:
        y = screenHeight - positionBuffer
        print "Y cursor position is set to maximum of", screenWidth - positionBuffer

    # set clock
    clock = pygame.time.Clock()

    # set screen size
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # clear screen
    screen.fill(white)

    # print out instructions
    print "\nInstructions: "
    print "Use the arrow keys to draw on the screen"
    print "Hit 'C' to clear the screen"
    print "Hit 'Q' to quit the game"

    while 1:
        # keep game at max 80 fps
        clock.tick(fps)

        # draw the initial dot on the screen
        pygame.draw.circle(screen, black, (x,y), dotSize)
        pygame.display.update()

        # handle a key being pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] : x += 1
        if key[pygame.K_LEFT] : x -= 1
        if key[pygame.K_UP] : y -= 1
        if key[pygame.K_DOWN] : y += 1
        if key[pygame.K_q] : sys.exit()
        if key[pygame.K_c] : screen.fill(white)

        # handle special case for quit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

if __name__ == "__main__":
    main()