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


wave = 0
enemies = []
enemies_spawn = []
wave_start = False
wave_spawn = False
last_spawn = pygame.time.get_ticks()


running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    wave_font = pygame.font.Font('freesansbold.ttf', 32)
    wave_text = wave_font.render(f"Wave: {wave}", True, (0, 0, 0))
    screen.blit(wave_text, (10, 10))
    
    time_passed = pygame.time.get_ticks()

    if time_passed > 15000 and wave_start == False:
        wave +=1
        wave_start = True

    if wave > 0 and wave > 10 and wave_spawn == False:
        for x in range(0, wave):
            enemies_spawn.append(Enemy1())
    elif wave > 9 and wave > 20 and wave_spawn == False:
        for x in range(0, wave):
            enemies_spawn.append(Enemy2())
    elif wave > 19 and wave > 30 and wave_spawn == False:
        for x in range(0, wave):
            enemies_spawn.append(Enemy3())
    elif wave > 29 and wave > 40 and wave_spawn == False:
        for x in range(0, wave):
            enemies_spawn.append(Enemy4())
    elif wave == 40 and wave_spawn == False:
            enemies_spawn.append(Boss())

    if time_passed - last_spawn > 2000 and len(enemies_spawn) != 0:
        enemies.append(enemies_spawn[0])
        screen.blit(enemies_spawn[0], (438, 864))
        last_spawn = pygame.time.get_ticks()
    

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