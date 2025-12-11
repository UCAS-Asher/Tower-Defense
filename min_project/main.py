#Tower Defense Game - Complete Implementation

from min_classes import *
import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
FPS = 60
GRID_SIZE = 60

# Initialize game
game = Map()
user = User(health=500, money=100)

# Set background
background = game.image

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
pygame_icon = pygame.image.load('resources/background/icon.png')
pygame.display.set_icon(pygame_icon)

# Clock for FPS
clock = pygame.time.Clock()

# Game variables
wave = 0
enemies = []
enemies_spawn = []
wave_start = False
wave_spawn = False
last_spawn = 0
game_over = False
game_won = False
selected_tower = None
tower_placement_mode = False
current_wave_time = 0
wave_complete = False
last_wave_time = 0

# Simple path for enemies (curved path across the map)
enemy_path = [
    (438, 864),  # Start
    (438, 750),
    (400, 650),
    (350, 600),
    (250, 580),
    (150, 590),
    (100, 650),
    (150, 750),
    (200, 850),
    (300, 900),
    (438, 900),  # End
]

# Fonts
wave_font = pygame.font.Font('freesansbold.ttf', 32)
small_font = pygame.font.Font('freesansbold.ttf', 24)
tiny_font = pygame.font.Font('freesansbold.ttf', 16)

def draw_ui():
    """Draw UI elements on screen"""
    # Wave text
    wave_text = wave_font.render(f"Wave: {wave}", True, (255, 255, 255))
    screen.blit(wave_text, (10, 10))
    
    # Health text
    health_color = (255, 0, 0) if user.health < 100 else (0, 255, 0)
    health_text = small_font.render(f"Health: {user.health}", True, health_color)
    screen.blit(health_text, (10, 50))
    
    # Money text
    money_text = small_font.render(f"Money: {user.money}", True, (255, 215, 0))
    screen.blit(money_text, (10, 90))
    
    # Tower placement mode indicator
    if tower_placement_mode and selected_tower:
        mode_text = tiny_font.render(f"Placing: {selected_tower.__class__.__name__} (Click to place, ESC to cancel)", True, (255, 255, 0))
        screen.blit(mode_text, (10, 900))

def spawn_wave():
    """Spawn enemies for the current wave"""
    global wave_spawn, enemies_spawn
    wave_spawn = True
    enemies_spawn = []
    
    # Wave progression
    if wave <= 5:
        count = wave + 2
        for _ in range(count):
            enemies_spawn.append(Enemy1())
    elif wave <= 10:
        count = wave
        for _ in range(count):
            enemies_spawn.append(Enemy2())
    elif wave <= 15:
        count = wave - 3
        for _ in range(count):
            enemies_spawn.append(Enemy3())
    elif wave <= 19:
        count = wave - 10
        for _ in range(count):
            enemies_spawn.append(Enemy4())
    elif wave == 20:
        enemies_spawn.append(Boss())
    else:
        # Victory
        return True
    
    return False

def show_menu():
    """Display tower selection menu"""
    menu_items = [
        ("1", "Tower1", 50),
        ("2", "Tower2", 125),
        ("3", "Tower3", 500),
        ("4", "Tower4", 800),
        ("5", "Tower5", 1250),
        ("6", "Tower6", 2500),
    ]
    
    tower_display = "Available Towers: "
    for key, name, cost in menu_items:
        tower_display += f"[{key}:{name}(${cost})] "
    
    menu_text = tiny_font.render(tower_display, True, (200, 200, 200))
    screen.blit(menu_text, (10, 930))

def handle_tower_placement(mouse_pos):
    """Handle tower placement on click"""
    global tower_placement_mode, selected_tower
    
    x, y = mouse_pos
    # Snap to grid
    grid_x = (x // GRID_SIZE) * GRID_SIZE
    grid_y = (y // GRID_SIZE) * GRID_SIZE
    
    # Create tower instance
    tower_classes = [Tower1, Tower2, Tower3, Tower4, Tower5, Tower6]
    if selected_tower.__class__ in tower_classes:
        tower = selected_tower.__class__(grid_x, grid_y)
        if game.place_tower(tower, user, screen):
            tower_placement_mode = False
            selected_tower = None
            return True
    
    return False

def handle_key_press(event):
    """Handle keyboard input for tower selection"""
    global tower_placement_mode, selected_tower
    
    if event.type == pygame.KEYDOWN:
        tower_map = {
            pygame.K_1: Tower1(0, 0),
            pygame.K_2: Tower2(0, 0),
            pygame.K_3: Tower3(0, 0),
            pygame.K_4: Tower4(0, 0),
            pygame.K_5: Tower5(0, 0),
            pygame.K_6: Tower6(0, 0),
        }
        
        if event.key in tower_map:
            selected_tower = tower_map[event.key]
            tower_placement_mode = True
        elif event.key == pygame.K_ESCAPE:
            tower_placement_mode = False
            selected_tower = None

# Main game loop
running = True
start_time = pygame.time.get_ticks()

while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000  # Convert to seconds
    
    # Fill screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    # Check game over
    if not user.check_zone():
        game_over = True
        game_over_text = wave_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(game_over_text, (400, 450))
    
    # Check game won
    if game_won:
        won_text = wave_font.render("YOU WIN!", True, (0, 255, 0))
        screen.blit(won_text, (380, 450))
    
    # Start waves
    if elapsed_time > 3 and wave == 0:
        wave = 1
        wave_start = True
        last_wave_time = current_time
    elif wave_complete and (current_time - last_wave_time) > 5000:
        if spawn_wave() == True:
            game_won = True
        else:
            wave += 1
            wave_complete = False
            last_wave_time = current_time
    
    # Spawn enemies
    if wave_spawn and len(enemies_spawn) > 0 and (current_time - last_spawn) > 1000:
        enemies.append(enemies_spawn.pop(0))
        last_spawn = current_time
        
        if len(enemies_spawn) == 0:
            wave_spawn = False
            wave_complete = True
    
    # Move enemies
    for enemy in enemies[:]:
        if enemy.alive:
            enemy.move(enemy_path)
            screen.blit(enemy.image, (int(enemy.x), int(enemy.y)))
            
            # Draw health bar
            health_width = 30
            health_ratio = enemy.hp / enemy.max_hp
            pygame.draw.rect(screen, (255, 0, 0), (int(enemy.x), int(enemy.y) - 10, health_width, 4))
            pygame.draw.rect(screen, (0, 255, 0), (int(enemy.x), int(enemy.y) - 10, int(health_width * health_ratio), 4))
            
            # Check if reached end
            if enemy.path_index >= len(enemy_path) - 1:
                enemy.hit_zone(user)
                enemy.alive = False
        else:
            enemy.give_money(user)
            enemies.remove(enemy)
    
    # Tower shooting
    for tower in game.towers:
        target = tower.shoot(enemies, current_time)
        screen.blit(tower.image, (tower.x, tower.y))
        
        # Draw range radius (optional, for debugging)
        # pygame.draw.circle(screen, (100, 100, 100), (int(tower.x + 30), int(tower.y + 30)), tower.range_radius, 1)
    
    # Tower placement preview
    if tower_placement_mode and selected_tower:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x = (mouse_x // GRID_SIZE) * GRID_SIZE
        grid_y = (mouse_y // GRID_SIZE) * GRID_SIZE
        
        # Draw semi-transparent preview
        preview_image = selected_tower.image
        preview_surface = preview_image.copy()
        preview_surface.set_alpha(128)
        screen.blit(preview_surface, (grid_x, grid_y))
        
        # Draw range circle
        pygame.draw.circle(screen, (100, 200, 100), (grid_x + 30, grid_y + 30), selected_tower.range_radius, 1)
    
    # Draw UI
    draw_ui()
    show_menu()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            handle_key_press(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN and tower_placement_mode:
            if event.button == 1:  # Left click
                handle_tower_placement(event.pos)
    
    pygame.display.flip()

pygame.quit()
