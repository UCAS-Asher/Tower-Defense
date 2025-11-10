from abc import ABC, abstractmethod

class Map():
    def __init__(self, x_spots = 12, y_spots = 12, towers = [], enemies = [], wave = 0):
        self.image = ""
        self.music = ""
        self.x_spots = x_spots
        self.y_spots = y_spots
        self.towers = towers
        self.enemies = enemies
        self.wave = wave

    def place_tower(self):
        pass

    def spawn_enemy(self):
        pass

    def wave_money(self, user):
        user.money += ((self.wave*15) + 10)

class User():
    def __init__(self, health = 500, money = 75):
        self.health = health
        self.money = money

    def check_zone(self):
        if self.health > 0:
            return True
        else:
            return False


class Enemy(ABC):
    def __init__(self, hp, max_hp, speed, image):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image

    
    def hit_zone(self, user):
        user.health -= self.max_hp*0.5
        
    
    @abstractmethod
    def give_money(self):
        pass


class Enemy1(Enemy):
    def __init__(self, hp = 100, max_hp = 100, speed = 0.3, image = ''):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image
    
    def give_money(self, user):
        user.money += self.max_hp*0.5

class Enemy2(Enemy):
    def __init__(self, hp = 200, max_hp = 200, speed = 0.35, image = ''):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image
    
    def give_money(self, user):
        user.money += self.max_hp*0.5