import pygame
from PlayersTank import PlayerTank
from game_assets import walls, eagle, explosion, blast, fire, bonus
import Level3Map

brick, stone = walls()
eagle1, eagle2, eagle3, eagle4, eagle5 = eagle()
explosion_sound = explosion()
blast1, blast2, blast3, blast4, blast5, blast6, blast7, blast8 = blast()
fire_sound = fire()
bonusgun, bonustank, bonusstar, bonusstone = bonus()

pygame.init()

TILE_SIZE = 32

map_layout = [
    [' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    [' ', ' ', 'S', 'B', 'S', 'S', ' ', 'B', ' ', 'B', 'B', 'S', 'B', 'S', ' ', 'S', ' ', 'S', 'S', 'S', 'S', 'S', ' ', 'S', 'T', 'S'],
    ['S', ' ', 'S', 'B', ' ', 'S', 'B', 'S', 'B', 'S', 'B', 'B', 'B', 'S', ' ', 'S', 'B', 'S', 'B', ' ', 'B', ' ', ' ', ' ', ' ', 'S'],
    ['S', ' ', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'S', 'S', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'S', 'B', 'S', ' ', 'S', ' ', 'S'],
    ['S', ' ', 'B', ' ', 'B', 'S', 'B', 'S', ' ', ' ', 'S', ' ', ' ', 'S', 'B', 'S', 'B', ' ', 'B', 'S', ' ', 'S', ' ', 'S', ' ', 'S'],
    ['S', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'S', ' ', 'S', 'B', 'B', 'S', 'B', 'S', 'S', 'S', 'S', 'S', 'B', 'S', 'S', 'S', 'S', 'S'],
    ['S', ' ', 'B', 'B', 'B', 'B', ' ', ' ', 'S', 'B', 'S', ' ', ' ', 'S', 'B', 'S', ' ', ' ', ' ', 'B', ' ', 'S', 'B', 'B', ' ', 'S'],
    ['S', ' ', 'S', 'S', 'S', 'S', 'S', ' ', 'S', 'B', 'B', 'S', 'B', 'S', ' ', 'S', 'B', 'S', 'S', 'S', 'S', 'S', ' ', 'S', ' ', 'S'],
    ['S', ' ', 'B', ' ', 'B', 'S', 'B', 'B', 'S', 'S', ' ', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'B', ' ', 'S', ' ', 'S', ' ', 'S'],
    ['S', 'S', 'S', 'S', 'B', 'S', 'B', 'B', ' ', 'B', 'B', 'S', 'B', 'B', 'B', 'S', 'B', 'B', ' ', 'S', ' ', 'S', 'B', 'S', 'B', 'S'],
    ['S', ' ', 'B', 'S', 'B', 'S', 'S', 'S', 'S', 'B', 'S', 'S', 'B', 'S', 'S', 'S', ' ', 'S', 'B', 'S', 'B', 'S', 'B', 'S', 'B', 'S'],
    ['S', ' ', 'B', ' ', 'B', ' ', 'B', 'S', ' ', ' ', 'B', 'S', 'B', 'B', 'B', 'S', 'S', 'S', ' ', 'S', ' ', 'B', 'B', 'S', 'B', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'S', 'B', 'B', 'B', ' ', 'B', 'S', 'S', 'S', 'S', 'S', ' ', 'S', 'B', 'S'],
    ['S', ' ', 'S', 'B', 'B', 'B', ' ', 'S', 'B', 'S', 'S', 'S', 'S', 'S', ' ', ' ', 'B', ' ', 'S', ' ', ' ', 'B', 'B', 'S', ' ', 'S'],
    ['S', ' ', 'S', 'B', 'S', 'B', 'S', 'S', ' ', 'S', 'B', ' ', 'B', 'S', 'S', 'S', 'S', 'S', 'S', ' ', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'B', 'S', 'S', 'S', 'B', 'B', 'S', 'S', 'S', ' ', 'B', 'B', 'B', 'B', 'S', 'B', ' ', ' ', ' ', 'S', 'B', 'B', 'B', 'ST', 'S'],
    ['S', 'B', 'S', 'B', 'S', ' ', 'B', ' ', 'B', 'B', 'B', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'S', 'S', 'S', 'B', 'S', 'S', 'S', 'S'],
    ['S', 'B', 'S', 'B', 'S', 'S', 'B', 'S', 'S', 'S', ' ', 'S', ' ', 'S', 'B', 'S', 'B', 'B', 'B', 'S', ' ', 'B', 'B', ' ', ' ', 'S'],
    ['S', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'S', ' ', 'B', 'S', 'B', 'S', 'B', 'S', 'S', 'S', 'B', 'S', 'B', 'S', ' ', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'B', 'S', ' ', 'B', 'S', 'B', 'B', 'B', 'S', 'B', 'S', ' ', 'S', 'B', 'B', 'B', 'S'],
    ['S', 'B', ' ', 'B', 'S', ' ', 'S', ' ', 'S', ' ', 'S', 'B', 'B', 'S', 'S', 'S', 'B', 'S', ' ', 'B', 'B', 'S', 'B', 'S', 'B', 'S'],
    ['S', ' ', 'S', 'B', 'B', 'B', 'S', 'B', 'S', 'B', 'S', 'B', 'B', ' ', 'S', 'S', 'B', 'S', 'B', 'S', ' ', 'S', 'B', 'S', ' ', 'S'],
    ['S', 'G', 'S', ' ', 'B', 'B', 'S', ' ', 'S', ' ', ' ', 'B', 'S', ' ', 'B', 'S', 'B', 'B', 'B', 'S', 'B', 'S', 'BS', 'S', 'E5', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
]


SCREEN_WIDTH = len(map_layout[0]) * TILE_SIZE
SCREEN_HEIGHT = len(map_layout) * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tanks Map")

player_tank = PlayerTank(0, 0)


def check_collision(new_x, new_y, map_layout):
    # Create a tank rectangle using the actual tank size (50x50)
    player_tank = pygame.Rect(new_x, new_y, 23, 23)  # 50x50 based on your scaled tank size

    # Check map bounds (tank shouldn't go out of screen)
    if not (0 <= player_tank.left < SCREEN_WIDTH and 0 <= player_tank.top < SCREEN_HEIGHT):
        return True

    # Check for collision with tiles (B, S, E1, E2, E3, E4)
    for row_idx, row in enumerate(map_layout):
        for col_idx, tile in enumerate(row):
            x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
            tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

            # If the tile is one of the collidable ones (B, S, E1, E2, E3, E4), check for collision
            if tile in ['B', 'S', 'E1', 'E2', 'E3', 'E4', 'E5', 'G', 'T', 'ST', 'BS'] and player_tank.colliderect(tile_rect):
                return True  # If collision occurs, return True (no movement)

    return False  # No collision, safe to move

# Define the global variables
eagle_destroyed = False
last_eagle_pos = None  # To store the last destroyed eagle's position

def handle_bullet_collisions(bullets, map_layout):
    global eagle_destroyed, last_eagle_pos  # Access global variables
    
    for bullet in bullets[:]:  # Iterate over a copy of the list
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        
        for row_idx, row in enumerate(map_layout):
            for col_idx, tile in enumerate(row):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                # Check for collision with bricks
                if tile == 'B' and bullet_rect.colliderect(tile_rect):
                    map_layout[row_idx][col_idx] = ' '  # Remove the brick
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    explosion_sound.play()  # Play explosion sound
                    break  # Exit inner loop to avoid modifying the list during iteration

                if tile == 'T' and bullet_rect.colliderect(tile_rect):
                    map_layout[row_idx][col_idx] = ' '  # Remove the specific 'T' tile
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    explosion_sound.play()  # Play explosion sound
                    
                    # After destroying 'T', destroy all 'B' tiles on the map
                    for row_idx, row in enumerate(map_layout):
                        for col_idx, tile in enumerate(row):
                            if tile == 'B':  # Check for brick tiles ('B')
                                map_layout[row_idx][col_idx] = ' '  # Remove the brick
                    explosion_sound.play()  # Play explosion sound for all destroyed bricks
                    
                    break

                if tile == 'G' and bullet_rect.colliderect(tile_rect):
                    map_layout[row_idx][col_idx] = ' '  # Remove the brick
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    explosion_sound.play()  # Play explosion sound
                    player_tank.collect_power_up()
                    break  # Exit inner loop to avoid modifying the list during iteration

                if tile == 'ST' and bullet_rect.colliderect(tile_rect):
                    # First, remove the 'ST' (stone + tank) tile
                    map_layout[row_idx][col_idx] = ' '  # Remove the 'ST' tile
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    explosion_sound.play()  # Play explosion sound
                    
                    # Make all 'S' tiles breakable (turn all 'S' to 'B')
                    for row_idx in range(len(map_layout)):
                        for col_idx in range(len(map_layout[row_idx])):
                            if map_layout[row_idx][col_idx] == 'S':  # Check for 'S' tiles
                                map_layout[row_idx][col_idx] = 'B'  # Turn 'S' into 'B'

                    break

                if tile == 'BS' and bullet_rect.colliderect(tile_rect):
                    map_layout[row_idx][col_idx] = ' '  # Remove the specific 'BS' tile
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    explosion_sound.play()  # Play explosion sound
                    
                    # Reset the player's position to (0, 0)
                    player_tank.x, player_tank.y = 0, 0  # Update player's position
                    
                    break

                # Check for collision with stones
                if tile == 'S' and bullet_rect.colliderect(tile_rect):
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    return  # Exit the function as the bullet hit a stone
                
                # Check for collision with eagles
                if tile in ['E1', 'E2', 'E3', 'E4', 'E5'] and bullet_rect.colliderect(tile_rect):
                    map_layout[row_idx][col_idx] = ' '  # Remove the eagle
                    eagle_destroyed = True  # Set the flag that an eagle was destroyed
                    last_eagle_pos = (x, y)  # Store the position of the last destroyed eagle
                    if bullet in bullets:  # Check if the bullet is still in the list
                        bullets.remove(bullet)  # Remove the bullet
                    break  # Exit inner loop to avoid modifying the list during iteration

    # If an eagle was destroyed, remove all eagles from the map layout
    if eagle_destroyed:
        for row_idx, row in enumerate(map_layout):
            for col_idx, tile in enumerate(row):
                if tile in ['E1', 'E2', 'E3', 'E4', 'E5']:
                    map_layout[row_idx][col_idx] = ' '  # Remove the eagle

        explosion_sound.play()  # Play explosion sound
        
        # Trigger the explosion animation at the last eagle's position
        if last_eagle_pos:
            animate_blast(last_eagle_pos[0], last_eagle_pos[1])
        
        # Trigger Game Over if an eagle is hit
        game_over()

def check_eagle_visibility(eagle_x, eagle_y, screen_width, screen_height):
    global eagle_destroyed  # Access global variable

    # Check if eagle is off-screen
    if eagle_x < 0 or eagle_x > screen_width or eagle_y < 0 or eagle_y > screen_height:
        eagle_destroyed = True  # Set the flag if the eagle is off-screen


def animate_blast(x, y):
    blast_images = [blast1, blast2, blast3, blast4, blast5, blast6, blast7, blast8]
    frame_delay = 50  # Delay in milliseconds between frames for quick animation
    frame_count = len(blast_images)
    
    # Loop through the blast frames
    for i in range(frame_count):
        screen.fill((0, 0, 0))  # Clear the screen
        draw_map()  # Redraw the map
        
        # Draw the current blast frame at the position of the death
        screen.blit(blast_images[i], (x, y))
        
        # Update the display
        pygame.display.flip()
        
        # Delay between frames to control the animation speed
        pygame.time.delay(frame_delay)

def draw_gradient_rect(surface, rect, start_color, end_color):
    """Draw a vertical gradient rectangle."""
    x, y, width, height = rect
    for i in range(height):
        blend_ratio = i / height
        r = start_color[0] + (end_color[0] - start_color[0]) * blend_ratio
        g = start_color[1] + (end_color[1] - start_color[1]) * blend_ratio
        b = start_color[2] + (end_color[2] - start_color[2]) * blend_ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (x, y + i), (x + width, y + i))

def game_over():
    """Display Game Over screen with a 'Next' button."""
    font = pygame.font.Font(None, 74)
    text = font.render("MISSION COMPLETED!", True, (255, 0, 0))

    # Button font and text configuration
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("Next Level", True, (255, 255, 255))

    # Button rectangle setup
    button_width = button_text.get_width() + 20
    button_height = button_text.get_height() + 20
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + 100, button_width, button_height)

    # Button colors
    button_gradient_start = (255, 100, 100)  # Light red gradient start
    button_gradient_end = (255, 0, 0)  # Dark red gradient end
    hover_gradient_start = (255, 150, 150)  # Lighter red for hover effect
    hover_gradient_end = (255, 50, 50)  # Darker red for hover effect

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up screen (if not set globally)

    # Main game over screen loop
    screen.fill((0, 0, 0))  # Fill screen with black
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Draw the button with gradient (default)
    draw_gradient_rect(screen, button_rect, button_gradient_start, button_gradient_end)
    screen.blit(button_text, (button_rect.x + (button_rect.width // 2) - (button_text.get_width() // 2),
                             button_rect.y + (button_rect.height // 2) - (button_text.get_height() // 2)))

    pygame.display.flip()  # Update display

    waiting_for_click = True
    while waiting_for_click:
        mouse_pos = pygame.mouse.get_pos()  # Get mouse position

        # Check if the mouse is hovering over the button
        if button_rect.collidepoint(mouse_pos):
            # Draw the button with hover effect
            draw_gradient_rect(screen, button_rect, hover_gradient_start, hover_gradient_end)
        else:
            # Draw the default button
            draw_gradient_rect(screen, button_rect, button_gradient_start, button_gradient_end)

        # Re-draw text on top of the button
        screen.blit(button_text, (button_rect.x + (button_rect.width // 2) - (button_text.get_width() // 2),
                                 button_rect.y + (button_rect.height // 2) - (button_text.get_height() // 2)))

        pygame.display.flip()  # Update display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit the game if the window is closed
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting_for_click = False  # Exit loop when button is clicked
                    # Call the next level/start function (e.g., Level2Map.start())
                    Level3Map.start()
                    print("Next Level")  # Placeholder for your next level function

    pygame.quit()


def draw_map():
    """Draw the map, including bricks, stones, and eagles."""
    for row_idx, row in enumerate(map_layout):
        for col_idx, tile in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            if tile == 'B':  # Brick
                screen.blit(brick, (x, y))
            elif tile == 'S':  # Stone
                screen.blit(stone, (x, y))
            elif tile == 'E1':  # Eagle
                screen.blit(eagle1, (x, y))
            elif tile == 'E2':  # Eagle
                screen.blit(eagle2, (x, y))
            elif tile == 'E3':  # Eagle
                screen.blit(eagle3, (x, y))
            elif tile == 'E4':  # Eagle
                screen.blit(eagle4, (x, y))
            elif tile == 'E5':  # Eagle
                screen.blit(eagle5, (x, y))
            elif tile == 'G':  # Eagle
                screen.blit(bonusgun, (x, y))
            elif tile == 'T':  # Eagle
                screen.blit(bonustank, (x, y))
            elif tile == 'ST':  # Eagle
                screen.blit(bonusstar, (x, y))
            elif tile == 'BS':  # Eagle
                screen.blit(bonusstone, (x, y))

def start():
    """Initialize the game and start the game loop."""
    # Reset player tank to its starting position (e.g., top-left corner)
    player_tank.x = 0
    player_tank.y = 0
    player_tank.bullets.clear()  # Clear any previous bullets from the player

    # Reset the map layout if necessary (e.g., reload the map)
    # For example, you can recreate the map layout or reset specific elements:
    # map_layout = original_map_layout  # If you have a saved version of the initial layout

    # Run the main game loop
    game_loop()  # Make sure game_loop() is called once and that quitting happens only after it finishes


def game_loop():
    """Main game loop."""
    running = True
    last_fire_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the loop and quit the game

        if not pygame.get_init():  # Check if pygame is initialized before rendering
            break  # Exit the loop if Pygame is not initialized (e.g., window closed)

        screen.fill((0, 0, 0))  # Fill the screen with black

        # Get the current keys pressed
        keys = pygame.key.get_pressed()

        # Store the tank's current position before attempting to move
        prev_x, prev_y = player_tank.x, player_tank.y

        # Move the player tank based on key presses (existing movement logic)
        player_tank.tank_moved = player_tank.move(keys)

        # Check if the new position collides with bricks, stones, or eagles
        if check_collision(player_tank.x, player_tank.y, map_layout):
            # If there is a collision, revert the tank to its previous position
            player_tank.x, player_tank.y = prev_x, prev_y

        # Fire the bullet when the spacebar is pressed
        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
            if current_time - last_fire_time >= 800:  # If 1 second has passed
                player_tank.fire()  # Fire the bullet
                fire_sound.play()  # Play the fire sound
                last_fire_time = current_time

        # Handle bullet collisions (same as before)
        handle_bullet_collisions(player_tank.bullets, map_layout)

        # Draw the map and the player tank
        draw_map()
        player_tank.draw(screen)  # Draw the player tank on the map

        # Draw bullets
        for bullet in player_tank.bullets:
            bullet.draw(screen)

        pygame.display.update()  # Update the screen

    pygame.quit()  # Quit Pygame after exiting the loop
