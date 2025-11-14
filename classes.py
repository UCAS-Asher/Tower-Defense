from abc import ABC, abstractmethod

class Map():
    def __init__(self, x_spots = 16, y_spots = 16, towers = [], enemies = [], wave = 0):
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


#Enemies
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

class Enemy3(Enemy):
    def __init__(self, hp = 500, max_hp = 500, speed = 0.4, image = ''):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image
    
    def give_money(self, user):
        user.money += self.max_hp*0.5

class Enemy4(Enemy):
    def __init__(self, hp = 1500, max_hp = 1500, speed = 0.35, image = ''):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image
    
    def give_money(self, user):
        user.money += self.max_hp*0.5

class Boss(Enemy):
    def __init__(self, hp = 15000, max_hp = 15000, speed = 0.4, image = ''):
        self.hp = hp
        self.max_hp = max_hp
        self.speed = speed
        self.image = image
    
    def give_money(self, user):
        user.money += self.max_hp*0.5


#Projectiles
class Projectile():
    def __init__(self, image, sound):
        self.image = image
        self.sound = sound

    def shoot(self, enemy):
        pass



#Towers
class Tower(ABC):
    def __init__(self, damage, hit_speed, cost, image, bullet, sound):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
        self.projectile = Projectile(bullet, sound)
    
    def shoot(self, enemy):
        self.projectile.shoot(enemy)
        
    def upgrade(self, user):
        if user.money >= self.cost*2:
            user.money -= self.cost*2
            self.damage += self.damage*0.5
            self.hit_speed -= 0.05
            return True
        else:
            return False
    
    def upgrade2(self, user):
        if user.money >= self.cost*4:
            user.money -= self.cost*4
            self.damage += self.damage*0.5
            self.hit_speed -= 0.05
            return True
        else:
            return False
        
    def upgrade3(self, user):
        if user.money >= self.cost*6:
            user.money -= self.cost*6
            self.damage += self.damage*0.5
            self.hit_speed -= 0.1
            return True
        else:
            return False
        
    def upgrade4(self, user):
        if user.money >= self.cost*8:
            user.money -= self.cost*8
            self.damage += self.damage*0.5
            self.hit_speed -= 0.1
            return True
        else:
            return False

class Tower1(Tower):
    def __init__(self, damage=25, hit_speed = 1, cost = 50, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
        self.projectile = Projectile(bullet, sound)
    
    def shoot(self):
        pass
        

class Tower2(Tower):
    def __init__(self, damage=35, hit_speed = 0.75, cost = 125, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
    
    def shoot(self):
        pass
        

class Tower3(Tower):
    def __init__(self, damage=75, hit_speed = 0.5, cost = 500, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
    
    def shoot(self):
        pass
        

class Tower4(Tower):
    def __init__(self, damage=350, hit_speed = 1.75, cost = 800, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
    
    def shoot(self):
        pass


class Tower5(Tower):
    def __init__(self, damage=125, hit_speed = 0.4, cost = 1250, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
    
    def shoot(self):
        pass


class Tower6(Tower):
    def __init__(self, damage=250, hit_speed = 0.5, cost = 2500, image = '', bullet = '', sound = ''):
        self.damage = damage
        self.hit_speed = hit_speed
        self.cost = cost
        self.image = image
    
    def shoot(self):
        pass
        