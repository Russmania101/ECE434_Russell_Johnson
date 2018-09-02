#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,400))

x = 300
y = 200

clock = pygame.time.Clock()
screen.fill((255,255,255))

while 1:
    clock.tick(60)

    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] : x+=1
    if key[pygame.K_LEFT] : x-=1
    if key[pygame.K_UP] : y-=1
    if key[pygame.K_DOWN] : y+=1
    if key[pygame.K_ESCAPE] : sys.exit()
    if key[pygame.K_SPACE] : screen.fill((255, 255, 255))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()