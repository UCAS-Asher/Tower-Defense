from abc import ABC, abstractmethod
import pygame
from pygame import mixer
import math

class Map():
    def __init__(self, x_spots = 16, y_spots = 16):
        self.image = pygame.transform.scale(pygame.image.load('resources/background/map.png'), (960,960))
        self.music = ""
        self.x_spots = x_spots
        self.y_spots = y_spots
        self.towers = []
        self.wave = 0

    def place_tower(self, tower, money):
        if money >= tower.cost:
            money -= tower.cost
            self.towers.append(tower)
            return money
        return False

    def remove_tower(self, tower):
        if tower in self.towers:
            self.towers.remove(tower)

    def spawn_enemy(self):
        pass

    def wave_money(self, wave):
        return ((wave*15) + 10)


#Enemies
class Enemy(ABC):
    def __init__(self, hp, max_hp, speed, x=410.5, y=836.5):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.x = x
        self.y = y

    def move(self):
        path = [
        (410.5, 836.5),  # Start
        (410.5, 692.5),
        (692.5, 692.5),
        (692.5, 506.5),
        (218.5, 506.5),
        (218.5, 218.5),
        (836.5, 218.5) # End
        ]

        if self.x > path[1][0] and self.y == path[0][1]:
            self.x -= self.speed
        if self.x == path[1][0] and self.y > path[1][1]:
            self.y -= self.speed
        if self.x < path[2][0] and self.y == path[1][1]:
            self.x += self.speed
        if self.x == path[2][0] and self.y > path[3][1]:
            self.y -= self.speed
        if self.x > path[4][0] and self.y == path[3][1]:
            self.x -= self.speed
        if self.x == path[4][0] and self.y > path[5][1]:
            self.y -= self.speed
        if self.x < path[6][0] and self.y == path[5][1]:
            self.x += self.speed

        
    @abstractmethod
    def give_money(self, user):
        pass


class Enemy1(Enemy):
    def __init__(self, hp = 100, max_hp = 100, speed = 1, x=410.5, y=836.5):
        super().__init__(hp, max_hp, speed, x, y)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy1.png'), (45,45))
    
    def give_money(self, user):
        user.add_money(int(self.max_hp*0.5))

class Enemy2(Enemy):
    def __init__(self, hp = 200, max_hp = 300, speed = 0.35, x=410.5, y=836.5):
        super().__init__(hp, max_hp, speed, x, y)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy2.png'), (50,50))
    
    def give_money(self, user):
        user.add_money(int(self.max_hp*0.35))

class Enemy3(Enemy):
    def __init__(self, hp = 500, max_hp = 900, speed = 0.4, x=410.5, y=836.5):
        super().__init__(hp, max_hp, speed, x, y)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy3.png'), (55,55))
    
    def give_money(self, user):
        user.add_money(int(self.max_hp*0.3))

class Enemy4(Enemy):
    def __init__(self, hp = 1500, max_hp = 1800, speed = 0.35, x=410.5, y=836.5):
        super().__init__(hp, max_hp, speed, x, y)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/enemy4.png'), (60,60))
    
    def give_money(self, user):
        user.add_money(int(self.max_hp*0.25))

class Boss(Enemy):
    def __init__(self, hp = 15000, max_hp = 15000, speed = 0.4, x=410.5, y=836.5):
        super().__init__(hp, max_hp, speed, x, y)
        self.image = pygame.transform.scale(pygame.image.load('resources/enemies/boss.png'), (65,65))
    
    def give_money(self, user):
        user.add_money(int(self.max_hp*100000000000000000000000000000000000000000000000000))



#Towers
class Tower(ABC):
    def __init__(self, x, y, damage, hit_speed, cost, range_radius=150):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.x = x
        self.y = y
        self.range_radius = range_radius
        self.last_shot_time = 0
        
    def can_shoot(self, current_time):
        return (current_time - self.last_shot_time) > (self.hit_speed * 1000)
    
    def shoot(self, enemies, current_time):
        if not self.can_shoot(current_time):
            return None
        
        closest_enemy = None
        closest_distance = self.range_radius
        
        for enemy in enemies:
            distance = math.sqrt((enemy.x - self.x)**2 + (enemy.y - self.y)**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_enemy = enemy
        
        if closest_enemy:
            self.last_shot_time = current_time
            closest_enemy.hp -= self.damage
            return closest_enemy
        return None
        
    def upgrade(self, user):
        if user.money >= self.cost*2:
            user.money -= self.cost*2
            self.damage += int(self.damage*0.5)
            self.hit_speed -= 0.05
            return True
        else:
            return False
    
    def upgrade2(self, user):
        if user.money >= self.cost*4:
            user.money -= self.cost*4
            self.damage += int(self.damage*0.5)
            self.hit_speed -= 0.05
            return True
        else:
            return False
        
    def upgrade3(self, user):
        if user.money >= self.cost*6:
            user.money -= self.cost*6
            self.damage += int(self.damage*0.5)
            self.hit_speed -= 0.1
            return True
        else:
            return False
        
    def upgrade4(self, user):
        if user.money >= self.cost*8:
            user.money -= self.cost*8
            self.damage += int(self.damage*0.5)
            self.hit_speed -= 0.1
            return True
        else:
            return False

class Tower1(Tower):
    def __init__(self, x, y, damage=25, hit_speed = 1, cost = 65, range_radius=160):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/broken_heart.png'), (60,60))
    

class Tower2(Tower):
    def __init__(self, x, y, damage=35, hit_speed = 0.75, cost = 250, range_radius=180):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/chickenstarsguy.png'), (60,60))
    

class Tower3(Tower):
    def __init__(self, x, y, damage=75, hit_speed = 0.5, cost = 750, range_radius=200):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/einstein.png'), (60,60))
    

class Tower4(Tower):
    def __init__(self, x, y, damage=350, hit_speed = 1.75, cost = 1900, range_radius=280):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/61guy.png'), (60,60))


class Tower5(Tower):
    def __init__(self, x, y, damage=125, hit_speed = 0.4, cost = 4250, range_radius=220):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/kendrick.png'), (60,60))


class Tower6(Tower):
    def __init__(self, x, y, damage=250, hit_speed = 0.5, cost = 12000, range_radius=240):
        super().__init__(x, y, damage, hit_speed, cost, range_radius)
        self.image = pygame.transform.scale(pygame.image.load('resources/towers/mason.png'), (60,60))
        