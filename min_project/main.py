#AW Final Project Code

from min_classes import *

import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

game = Map()

#set background
background = game.image

#background music
#mixer.music.load('resources\\background.wav')
#mixer.music.play(-1)

screen = pygame.display.set_mode((960, 960))
pygame.display.set_caption("Tower Defense")
pygame_icon = pygame.image.load('resources/background/icon.png')
#32x32 image
pygame.display.set_icon(pygame_icon)

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    
    #loop events
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_e]:
                state = True
        if event.type == pygame.KEYUP:
            if keys[pygame.K_e]:
                if state == True:
                    game.place_tower(screen, )
                    state = False
        
    pygame.display.flip()