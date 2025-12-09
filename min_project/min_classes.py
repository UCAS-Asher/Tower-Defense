from abc import ABC, abstractmethod
import pygame
from pygame import mixer

class Map():
    def __init__(self, x_spots = 16, y_spots = 16):
        self.image = pygame.transform.scale(pygame.image.load('resources/background/map.png'), (960,960))
        self.music = ""
        self.x_spots = x_spots
        self.y_spots = y_spots


    def place_tower(self, screen):
        pass

    def spawn_enemy(self):
        pass

    def wave_money(self, wave):
        #give user money based on wave number
        return ((wave * 15) + 10)



#Enemies
class Enemy(ABC):
    def __init__(self, hp, max_hp, speed):
        # default start position for enemies
        self.x = 410.5
        self.y = 836.5
        # track movement deltas as attributes (was local vars before)
        self.x_change = 0
        self.y_change = 0
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed

    
    def hit_zone(self, user):
        user.health -= self.max_hp*0.5
    
    def move(self):
        if self.x == 410.5 and self.y == 836.5:
            self.y_change = -self.speed
        elif self.y == 692.5 and self.x == 410.5:
            self.y_change = 0
            self.x_change = self.speed
        elif self.y == 692.5 and self.x == 692.5:
            self.x_change = 0
            self.y_change = -self.speed
        elif self.y == 506.5 and self.x == 692.5:
            self.y_change = 0
            self.x_change = -self.speed
        elif self.y == 506.5 and self.x == 218.5:
            self.x_change = 0
            self.y_change = -self.speed
        elif self.y == 218.5 and self.x == 218.5:
            self.y_change = 0
            self.x_change = self.speed
        elif self.y == 218.5 and self.x == 836.5:
            self.x_change = 0
            
    def give_money(self):
        money += self.max_hp*0.5
        return money


class Enemy1(Enemy):
    def __init__(self, hp = 100, max_hp = 100, speed = 6.0):
        # initialize base Enemy to get x/y and movement attributes
        super().__init__(hp, max_hp, speed)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy1.png'), (60,60))
    

class Enemy2(Enemy):
    def __init__(self, hp = 200, max_hp = 200, speed = 0.35):
        super().__init__(hp, max_hp, speed)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy2.png'), (60,60))
    

class Enemy3(Enemy):
    def __init__(self, hp = 500, max_hp = 500, speed = 0.4):
        super().__init__(hp, max_hp, speed)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy3.png'), (60,60))
    

class Enemy4(Enemy):
    def __init__(self, hp = 1500, max_hp = 1500, speed = 0.35, image = ''):
        super().__init__(hp, max_hp, speed)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy4.png'), (60,60))
    

class Boss(Enemy):
    def __init__(self, hp = 15000, max_hp = 15000, speed = 0.4, image = ''):
        super().__init__(hp, max_hp, speed)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/boss.png'), (65,65))
    


#Towers
class Tower(ABC):
    def __init__(self, x, y, damage, hit_speed, range, cost, image):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.x = x
        self.y = y
        self.last_shot = 0
        self.delay = int(1000 * hit_speed)  # milliseconds between shots
        self.image = image

    def place_tower(self, screen):
        while True:
            screen.blit(pygame.transform.scale(pygame.image.load('resources/pop_ups/place_map.png'), (960, 960)), (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 0 <= mouse_x <= 960 and 0 <= mouse_y <= 960:
                        #first row of spots
                        if 102 <= mouse_x <= 192 and 102 <= mouse_y <= 192:
                            self.x = 147
                            self.y = 147
                        elif 198 <= mouse_x <= 288 and 102 <= mouse_y <= 192:
                            self.x = 249
                            self.y = 147
                        elif 294 <= mouse_x <= 384 and 102 <= mouse_y <= 192:
                            self.x = 351
                            self.y = 147
                        elif 390 <= mouse_x <= 480 and 102 <= mouse_y <= 192:
                            self.x = 453
                            self.y = 147
                        elif 486 <= mouse_x <= 576 and 102 <= mouse_y <= 192:
                            self.x = 555
                            self.y = 147
                        elif 582 <= mouse_x <= 672 and 102 <= mouse_y <= 192:
                            self.x = 657
                            self.y = 147
                        elif 678 <= mouse_x <= 768 and 102 <= mouse_y <= 192:
                            self.x = 759
                            self.y = 147
                        elif 774 <= mouse_x <= 864 and 102 <= mouse_y <= 192:
                            self.x = 861
                            self.y = 147
                        #second row of spots
                        elif 102 <= mouse_x <= 192 and 198 <= mouse_y <= 288:
                            self.x = 147
                            self.y = 249
                        #third row of spots
                        elif 102 <= mouse_x <= 192 and 294 <= mouse_y <= 384:
                            self.x = 147
                            self.y = 351
                        elif 294 <= mouse_x <= 384 and 294 <= mouse_y <= 384:
                            self.x = 351
                            self.y = 351
                        elif 390 <= mouse_x <= 480 and 294 <= mouse_y <= 384:
                            self.x = 453
                            self.y = 351
                        elif 486 <= mouse_x <= 576 and 294 <= mouse_y <= 384:
                            self.x = 555
                            self.y = 351
                        elif 582 <= mouse_x <= 672 and 294 <= mouse_y <= 384:
                            self.x = 657
                            self.y = 351
                        elif 678 <= mouse_x <= 768 and 294 <= mouse_y <= 384:
                            self.x = 759
                            self.y = 351
                        elif 774 <= mouse_x <= 864 and 294 <= mouse_y <= 384:
                            self.x = 861
                            self.y = 351
                        #fourth row of spots
                        elif 102 <= mouse_x <= 192 and 390 <= mouse_y <= 480:
                            self.x = 147
                            self.y = 453
                        elif 294 <= mouse_x <= 384 and 390 <= mouse_y <= 480:
                            self.x = 351
                            self.y = 453
                        elif 390 <= mouse_x <= 480 and 390 <= mouse_y <= 480:
                            self.x = 453
                            self.y = 453
                        elif 486 <= mouse_x <= 576 and 390 <= mouse_y <= 480:
                            self.x = 555
                            self.y = 453
                        elif 678 <= mouse_x <= 768 and 390 <= mouse_y <= 480:
                            self.x = 759
                            self.y = 453
                        elif 774 <= mouse_x <= 864 and 390 <= mouse_y <= 480:
                            self.x = 861
                            self.y = 453
                        #fifth row of spots
                        elif 102 <= mouse_x <= 192 and 486 <= mouse_y <= 576:
                            self.x = 147
                            self.y = 555
                        elif 774 <= mouse_x <= 864 and 486 <= mouse_y <= 576:
                            self.x = 861
                            self.y = 555
                        #sixth row of spots
                        elif 102 <= mouse_x <= 192 and 582 <= mouse_y <= 672:
                            self.x = 147
                            self.y = 657
                        elif 198 <= mouse_x <= 288 and 582 <= mouse_y <= 672:
                            self.x = 249
                            self.y = 657
                        elif 294 <= mouse_x <= 384 and 582 <= mouse_y <= 672:
                            self.x = 351
                            self.y = 657
                        elif 390 <= mouse_x <= 480 and 582 <= mouse_y <= 672:
                            self.x = 453
                            self.y = 657
                        elif 486 <= mouse_x <= 576 and 582 <= mouse_y <= 672:
                            self.x = 555
                            self.y = 657
                        elif 582 <= mouse_x <= 672 and 582 <= mouse_y <= 672:
                            self.x = 657
                            self.y = 657
                        elif 774 <= mouse_x <= 864 and 582 <= mouse_y <= 672:
                            self.x = 861
                            self.y = 657
                        #seventh row of spots
                        elif 102 <= mouse_x <= 192 and 678 <= mouse_y <= 768:
                            self.x = 147
                            self.y = 759
                        elif 198 <= mouse_x <= 288 and 678 <= mouse_y <= 768:
                            self.x = 249
                            self.y = 759
                        elif 294 <= mouse_x <= 384 and 678 <= mouse_y <= 768:
                            self.x = 351
                            self.y = 759
                        elif 774 <= mouse_x <= 864 and 678 <= mouse_y <= 768:
                            self.x = 861
                            self.y = 759
                        #eighth row of spots
                        elif 102 <= mouse_x <= 192 and 774 <= mouse_y <= 864:
                            self.x = 147
                            self.y = 861
                        elif 198 <= mouse_x <= 288 and 774 <= mouse_y <= 864:
                            self.x = 249
                            self.y = 861
                        elif 294 <= mouse_x <= 384 and 774 <= mouse_y <= 864:
                            self.x = 351
                            self.y = 861
                        elif 486 <= mouse_x <= 576 and 774 <= mouse_y <= 864:
                            self.x = 555
                            self.y = 861
                        elif 582 <= mouse_x <= 672 and 774 <= mouse_y <= 864:
                            self.x = 657
                            self.y = 861
                        elif 678 <= mouse_x <= 768 and 774 <= mouse_y <= 864:
                            self.x = 759
                            self.y = 861
                        elif 774 <= mouse_x <= 864 and 774 <= mouse_y <= 864:
                            self.x = 861
                            self.y = 861
                        else:
                            print("Invalid placement. Please select a valid spot.")
                            continue
                        screen.blit(self.image, (self.x, self.y))
                if event.type == pygame.K_ESCAPE:
                    break
            pygame.display.flip()

    def shoot (self):
        pass
        
    def upgrade(self, money):
        if money >= self.cost*2:
            money -= self.cost*2
            self.range += self.range*0.10
            self.damage += self.damage*0.5
            self.hit_speed -= 0.05
            return True
        else:
            return False
    
    def upgrade2(self, money):
        if money >= self.cost*4:
            money -= self.cost*4
            self.range += self.range*0.10
            self.damage += self.damage*0.5
            self.hit_speed -= 0.05
            return True
        else:
            return False
        
    def upgrade3(self, money):
        if money >= self.cost*6:
            money -= self.cost*6
            self.range += self.range*0.10
            self.damage += self.damage*0.5
            self.hit_speed -= 0.1
            return True
        else:
            return False
        
    def upgrade4(self, money):
        if money >= self.cost*8:
            money -= self.cost*8
            self.range += self.range*0.10
            self.damage += self.damage*0.5
            self.hit_speed -= 0.1
            return True
        else:
            return False

class Tower1(Tower):
    def __init__(self, x, y, damage=25, hit_speed = 1, range = 400, cost = 50):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/broken_heart.png'), (60,60))
        self.x = x
        self.y = y
    
        

class Tower2(Tower):
    def __init__(self, x, y, damage=35, hit_speed = 0.75, range = 450, cost = 125):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/chickenstarsguy.png'), (60,60))
        self.x = x
        self.y = y
    
        

class Tower3(Tower):
    def __init__(self, x, y, damage=75, hit_speed = 0.5, range = 500, cost = 500):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/einstein.png'), (60,60))
        self.x = x
        self.y = y
    
        

class Tower4(Tower):
    def __init__(self, x, y, damage=350, hit_speed = 1.75, range = 700, cost = 800):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/61guy.png'), (60,60))
        self.x = x
        self.y = y
    


class Tower5(Tower):
    def __init__(self, x, y, damage=125, hit_speed = 0.4, range = 550, cost = 1250):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/kendrick.png'), (60,60))
        self.x = x
        self.y = y
    

class Tower6(Tower):
    def __init__(self, x, y, damage=250, hit_speed = 0.5, range = 600, cost = 2500):
        self.damage = damage
        self.hit_speed = hit_speed
        self.range = range
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/mason.png'), (60,60))
        self.x = x
        self.y = y
    
        