#Tower Defense Game - Complete Implementation

from min_classes import *
import pygame

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
FPS = 60

# Initialize game
game = Map()


# Set background
background = game.image

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
pygame_icon = pygame.image.load('resources/background/icon.png')
pygame.display.set_icon(pygame_icon)

# Clock for FPS
clock = pygame.time.Clock()


#Important
money = 75
health = 500

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

# Simple path for enemies to follow
enemy_path = [
    (410.5, 836.5),  # Start
    (410.5, 692.5),
    (692.5, 692.5),
    (692.5, 506.5),
    (218.5, 506.5),
    (218.5, 218.5),
    (218.5, 836.5)  # End
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
    health_color = (255, 0, 0) if health < 100 else (0, 255, 0)
    health_text = small_font.render(f"Health: {health}", True, health_color)
    screen.blit(health_text, (10, 50))
    
    # Money text
    money_text = small_font.render(f"Money: {money}", True, (255, 215, 0))
    screen.blit(money_text, (10, 90))
    
    # Tower placement mode indicator
    if tower_placement_mode and selected_tower:
        mode_text = tiny_font.render(f"Placing: {selected_tower.__class__.__name__} (Click to place, ESC to cancel)", True, (255, 255, 0))
        screen.blit(mode_text, (10, 900))


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

def grid_snap(mouse_x, mouse_y):
    """Snap coordinates to grid for tower placement"""
    if 102 <= mouse_x <= 192 and 102 <= mouse_y <= 192:
        grid_x = 147
        grid_y = 147
    elif 198 <= mouse_x <= 288 and 102 <= mouse_y <= 192:
        grid_x = 249
        grid_y = 147
    elif 294 <= mouse_x <= 384 and 102 <= mouse_y <= 192:
        grid_x = 351
        grid_y = 147
    elif 390 <= mouse_x <= 480 and 102 <= mouse_y <= 192:
        grid_x = 453
        grid_y = 147
    elif 486 <= mouse_x <= 576 and 102 <= mouse_y <= 192:
        grid_x = 555
        grid_y = 147
    elif 582 <= mouse_x <= 672 and 102 <= mouse_y <= 192:
        grid_x = 657
        grid_y = 147
    elif 678 <= mouse_x <= 768 and 102 <= mouse_y <= 192:
        grid_x = 759
        grid_y = 147
    elif 774 <= mouse_x <= 864 and 102 <= mouse_y <= 192:
        grid_x = 861
        grid_y = 147
    #second row of spots
    elif 102 <= mouse_x <= 192 and 198 <= mouse_y <= 288:
        grid_x = 147
        grid_y = 249
    #third row of spots
    elif 102 <= mouse_x <= 192 and 294 <= mouse_y <= 384:
        grid_x = 147
        grid_y = 351
    elif 294 <= mouse_x <= 384 and 294 <= mouse_y <= 384:
        grid_x = 351
        grid_y = 351
    elif 390 <= mouse_x <= 480 and 294 <= mouse_y <= 384:
        grid_x = 453
        grid_y = 351
    elif 486 <= mouse_x <= 576 and 294 <= mouse_y <= 384:
        grid_x = 555
        grid_y = 351
    elif 582 <= mouse_x <= 672 and 294 <= mouse_y <= 384:
        grid_x = 657
        grid_y = 351
    elif 678 <= mouse_x <= 768 and 294 <= mouse_y <= 384:
        grid_x = 759
        grid_y = 351
    elif 774 <= mouse_x <= 864 and 294 <= mouse_y <= 384:
        grid_x = 861
        grid_y = 351
    #fourth row of spots
    elif 102 <= mouse_x <= 192 and 390 <= mouse_y <= 480:
        grid_x = 147
        grid_y = 453
    elif 294 <= mouse_x <= 384 and 390 <= mouse_y <= 480:
        grid_x = 351
        grid_y = 453
    elif 390 <= mouse_x <= 480 and 390 <= mouse_y <= 480:
        grid_x = 453
        grid_y = 453
    elif 486 <= mouse_x <= 576 and 390 <= mouse_y <= 480:
        grid_x = 555
        grid_y = 453
    elif 678 <= mouse_x <= 768 and 390 <= mouse_y <= 480:
        grid_x = 759
        grid_y = 453
    elif 774 <= mouse_x <= 864 and 390 <= mouse_y <= 480:
        grid_x = 861
        grid_y = 453
    #fifth row of spots
    elif 102 <= mouse_x <= 192 and 486 <= mouse_y <= 576:
        grid_x = 147
        grid_y = 555
    elif 774 <= mouse_x <= 864 and 486 <= mouse_y <= 576:
        grid_x = 861
        grid_y = 555
    #sixth row of spots
    elif 102 <= mouse_x <= 192 and 582 <= mouse_y <= 672:
        grid_x = 147
        grid_y = 657
    elif 198 <= mouse_x <= 288 and 582 <= mouse_y <= 672:
        grid_x = 249
        grid_y = 657
    elif 294 <= mouse_x <= 384 and 582 <= mouse_y <= 672:
        grid_x = 351
        grid_y = 657
    elif 390 <= mouse_x <= 480 and 582 <= mouse_y <= 672:
        grid_x = 453
        grid_y = 657
    elif 486 <= mouse_x <= 576 and 582 <= mouse_y <= 672:
        grid_x = 555
        grid_y = 657
    elif 582 <= mouse_x <= 672 and 582 <= mouse_y <= 672:
        grid_x = 657
        grid_y = 657
    elif 774 <= mouse_x <= 864 and 582 <= mouse_y <= 672:
        grid_x = 861
        grid_y = 657
    #seventh row of spots
    elif 102 <= mouse_x <= 192 and 678 <= mouse_y <= 768:
        grid_x = 147
        grid_y = 759
    elif 198 <= mouse_x <= 288 and 678 <= mouse_y <= 768:
        grid_x = 249
        grid_y = 759
    elif 294 <= mouse_x <= 384 and 678 <= mouse_y <= 768:
        grid_x = 351
        grid_y = 759
    elif 774 <= mouse_x <= 864 and 678 <= mouse_y <= 768:
        grid_x = 861
        grid_y = 759
    #eighth row of spots
    elif 102 <= mouse_x <= 192 and 774 <= mouse_y <= 864:
        grid_x = 147
        grid_y = 861
    elif 198 <= mouse_x <= 288 and 774 <= mouse_y <= 864:
        grid_x = 249
        grid_y = 861
    elif 294 <= mouse_x <= 384 and 774 <= mouse_y <= 864:
        grid_x = 351
        grid_y = 861
    elif 486 <= mouse_x <= 576 and 774 <= mouse_y <= 864:
        grid_x = 555
        grid_y = 861
    elif 582 <= mouse_x <= 672 and 774 <= mouse_y <= 864:
        grid_x = 657
        grid_y = 861
    elif 678 <= mouse_x <= 768 and 774 <= mouse_y <= 864:
        grid_x = 759
        grid_y = 861
    elif 774 <= mouse_x <= 864 and 774 <= mouse_y <= 864:
        grid_x = 861
        grid_y = 861


    return grid_x, grid_y


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
    if health <= 0:
        game_over = True
        game_over_text = wave_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(game_over_text, (400, 450))
    
    # Check game won
    if game_won:
        won_text = wave_font.render("YOU WIN!", True, (0, 255, 0))
        screen.blit(won_text, (380, 450))

    if tower_placement_mode == True:
        screen.blit('resources/pop_ups/place_map.png' (0,0))
    
    
    
    
    # Move enemies
    for enemy in enemies:
        enemy.move(enemy_path)
        screen.blit(enemy.image, ((enemy.x), (enemy.y)))
        
            
        if enemy.x > 870:
                health -= (enemy.max_hp/2)
        elif enemy.hp < 0:
            money += (enemy.max_hp/2)
            enemies.remove(enemy)
    
    # Tower shooting
    
        
        # Draw range radius (optional, for debugging)
        # pygame.draw.circle(screen, (100, 100, 100), (int(tower.x + 30), int(tower.y + 30)), tower.range_radius, 1)
    
    # Tower placement preview
    if tower_placement_mode and selected_tower:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x, grid_y = grid_snap(mouse_x, mouse_y)
        
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
