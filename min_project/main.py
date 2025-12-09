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

health = 500
wave = 0
money = 75
towers = []
enemies = []
enemies_spawn = []
wave_start = False
wave_spawn = False
last_spawn = 0


running = True

while running:
    if health <= 0:
        print("Game Over !, You have lost all your health.")
        running = False
    
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    display_font = pygame.font.Font('freesansbold.ttf', 32)
    hp_text = display_font.render(f"Health: {health}", True, (0, 255, 0))
    wave_text = display_font.render(f"Wave: {wave}", True, (0, 0, 0))
    money_text = display_font.render(f"Money: {money}", True, (0, 200, 0))
    screen.blit(wave_text, (10, 10))
    screen.blit(money_text, (650, 10))
    screen.blit(hp_text, (350, 10))
    
    #for delays and stuff
    current_time = pygame.time.get_ticks()

    #delay before first wave
    if current_time > 5000 and wave_start == False:
        wave +=1
        wave_start = True

    # spawn the wave (populate enemies_spawn) only once per wave
    if wave_spawn == False:
        if wave > 0 and wave < 10:
            for x in range(wave):
                enemies_spawn.append(Enemy1())
            wave_spawn = True
        elif wave >= 10 and wave < 20:
            for x in range(wave-9):
                enemies_spawn.append(Enemy2())
            wave_spawn = True
        elif wave >= 20 and wave < 30:
            for x in range(wave-19):
                enemies_spawn.append(Enemy3())
            wave_spawn = True
        elif wave >= 30 and wave < 40:
            for x in range(wave-29):
                enemies_spawn.append(Enemy4())
            wave_spawn = True
        elif wave == 40:
            enemies_spawn.append(Boss())
            wave_spawn = True

    # spawn enemies from the spawn queue with a delay
    if current_time - last_spawn > 2000 and len(enemies_spawn) > 0:
        enemies.append(enemies_spawn[0])
        # remove the first element
        enemies_spawn.pop(0)
        last_spawn = pygame.time.get_ticks()
    
    for enemy in enemies:
        enemy.move()
        # move() sets x_change/y_change; add to position
        enemy.x = enemy.x + enemy.x_change
        enemy.y = enemy.y + enemy.y_change
        if enemy.y == 218.5 and enemy.x == 836.5:
            health -= enemy.max_hp*0.5
            enemies.remove(enemy)
        screen.blit(enemy.image, (enemy.x, enemy.y))

    for tower in towers:
        screen.blit(tower.image, (tower.x, tower.y))
        # check for enemies in range
        for enemy in enemies:
            distance = math.sqrt((math.pow((tower.x - enemy.x),2)) + (math.pow((tower.y - enemy.y),2)))
            if distance <= tower.range:
                # check if enough time has passed since last shot
                if current_time - tower.last_shot > tower.delay:
                    enemy.hp -= tower.damage
                    tower.last_shot = pygame.time.get_ticks()
                    if enemy.hp <= 0:
                        money = enemy.give_money(money)
                        enemies.remove(enemy)
    
    if len(enemies) == 0 and len(enemies_spawn) == 0 and wave_start == True:
        wave += 1
        wave_spawn = False

    placed = False

    #loop events
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if placed == False:
                if event.key == pygame.K_1 and money >= 50:
                    if 
                    
                    tower = Tower1()
                    towers.append(tower)
                    placed = True
                if event.key == pygame.K_2 and money >= 125:
                    tower = Tower2()
                    towers.append(tower)
                    placed = True
                if event.key == pygame.K_3 and money >= 500:
                    tower = Tower3()
                    towers.append(tower)
                    placed = True
                if event.key == pygame.K_4 and money >= 800:
                    tower = Tower4()
                    towers.append(tower)
                    placed = True
                if event.key == pygame.K_5 and money >= 1250:
                    tower = Tower5()
                    towers.append(tower)
                    placed = True
                if event.key == pygame.K_6 and money >= 2500:
                    tower = Tower6()
                    towers.append(tower)
                    placed = True
            

    pygame.display.flip()