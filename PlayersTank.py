import pygame
from game_assets import tank  # Assuming tank() returns the images
from Bullet import Bullet  # Import Bullet class from Bullet.py

# Assuming tank() returns the images for different directions
tankD, tankU, tankL, tankR, blink1, blink2 = tank()  # Load images

pygame.init()

TILE_SIZE = 32

map_layout = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', 'S', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', 'S', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['B', 'B', ' ', ' ', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B'],
    ['S', 'S', ' ', ' ', 'B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'B', 'B', ' ', ' ', 'S', 'S'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', ' ', 'B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'E1', 'E2', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'E3', 'E4', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # More rows of your map layout here...
]

# Screen dimensions based on map layout
SCREEN_WIDTH = len(map_layout[0]) * TILE_SIZE
SCREEN_HEIGHT = len(map_layout) * TILE_SIZE

# Set screen size to match map layout
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Tank on Map")

class PlayerTank:
    def __init__(self, x, y, speed=0.2):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.width = 50  # Tank width (scaled image)
        self.height = 50  # Tank height (scaled image)
        self.speed = speed  # Speed of the tank
        self.image = tankD  # Initial tank image (facing down)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Rect for collision detection
        self.direction = 'DOWN'  # Initial direction of the tank
        self.blink_toggle = False  # Toggle to alternate blink images
        self.blink_start_time = None  # Time when blinking starts
        self.tank_blinking = True  # Flag to indicate whether the tank is blinking
        self.tank_moved = False  # Flag to track if the tank has moved
        self.bullets = []  # List to store active bullets
        self.last_fire_time = 0  # Time of the last shot
        self.fire_cooldown = 200  # Cooldown time in milliseconds (0.7 seconds)
        self.double_shot = False  # Flag to indicate if the tank can shoot 2 bullets per spacebar press

    def collect_power_up(self):
        """Enable double shot ability for the player tank."""
        self.double_shot = True

    def check_collision(self, new_x, new_y):
        """Placeholder function to check if the tank collides with walls or obstacles."""
        if new_x < 0 or new_x + self.width > SCREEN_WIDTH or new_y < 0 or new_y + self.height > SCREEN_HEIGHT:
            return True  # Collision detected
        return False

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def move(self, keys):
        """Move the tank based on key presses and check for collisions."""
        tank_moved = False  # Flag to check if the tank has moved
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Move up
            new_y = self.y - self.speed
            if not self.check_collision(self.x, new_y):  # Check if new position is valid
                self.direction = 'UP'
                self.y = new_y
                tank_moved = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Move down
            new_y = self.y + self.speed
            if not self.check_collision(self.x, new_y):  # Check if new position is valid
                self.direction = 'DOWN'
                self.y = new_y
                tank_moved = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Move left
            new_x = self.x - self.speed
            if not self.check_collision(new_x, self.y):  # Check if new position is valid
                self.direction = 'LEFT'
                self.x = new_x
                tank_moved = True
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Move right
            new_x = self.x + self.speed
            if not self.check_collision(new_x, self.y):  # Check if new position is valid
                self.direction = 'RIGHT'
                self.x = new_x
                tank_moved = True

        # Update the tank's rectangle for collision detection
        self.rect.x = self.x
        self.rect.y = self.y

        return tank_moved  # Return if the tank has moved

    def fire(self):
        """Create a new bullet based on the tank's position and direction."""
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

        # Check if enough time has passed since the last shot
        if current_time - self.last_fire_time >= self.fire_cooldown:
            # Create a new bullet and add it to the list
            if self.direction == 'UP':
                bullet_x = self.x + 10  # Adjust as needed
                bullet_y = self.y - 5  # Adjust as needed
            elif self.direction == 'DOWN':
                bullet_x = self.x + 10
                bullet_y = self.y + 24
            elif self.direction == 'LEFT':
                bullet_x = self.x - 5
                bullet_y = self.y + 10
            elif self.direction == 'RIGHT':
                bullet_x = self.x + 25
                bullet_y = self.y + 10

            # Create and add the first bullet
            new_bullet = Bullet(bullet_x, bullet_y, self.direction, speed=0.3)
            self.bullets.append(new_bullet)

            # If the double_shot flag is enabled, create and add a second bullet
            if self.double_shot:
                if self.direction == 'UP':
                    bullet_y = self.y - 20  # Adjust as needed for second bullet
                elif self.direction == 'DOWN':
                    bullet_y = self.y + 34
                elif self.direction == 'LEFT':
                    bullet_x = self.x - 15
                elif self.direction == 'RIGHT':
                    bullet_x = self.x + 35

                # Create and add the second bullet
                new_bullet = Bullet(bullet_x, bullet_y, self.direction, speed=0.3)
                self.bullets.append(new_bullet)

            # Update the last fire time
            self.last_fire_time = current_time

    def draw(self, screen):
        """Draw the tank on the screen with blinking logic."""
        if self.tank_blinking:
            if self.blink_start_time is None:
                self.blink_start_time = pygame.time.get_ticks()

            # Alternate between blink1 and blink2
            if self.blink_toggle:
                screen.blit(blink1, (self.x, self.y))
            else:
                screen.blit(blink2, (self.x, self.y))

            if pygame.time.get_ticks() - self.blink_start_time > 100:
                self.blink_toggle = not self.blink_toggle
                self.blink_start_time = pygame.time.get_ticks()

            if self.tank_moved:
                self.tank_blinking = False
                self.tank_moved = False
                self.blink_toggle = False
                self.draw_tank(screen)
        else:
            self.draw_tank(screen)

        # Draw all bullets
        for bullet in self.bullets:
            bullet.move()  # Update the bullet's position
            bullet.draw(screen)  # Draw the bullet

    def draw_tank(self, screen):
        """Draw the tank facing in the current direction."""
        if self.direction == 'UP':
            screen.blit(tankU, (self.x, self.y))
        elif self.direction == 'DOWN':
            screen.blit(tankD, (self.x, self.y))
        elif self.direction == 'LEFT':
            screen.blit(tankL, (self.x, self.y))
        elif self.direction == 'RIGHT':
            screen.blit(tankR, (self.x, self.y))


# Only run the game loop if this file is being executed directly
if __name__ == "__main__":
    # Initialize the map screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Tank on Map")

    # Create an instance of PlayerTank at a starting position
    player_tank = PlayerTank(100, 100)

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        # Get the current keys pressed
        keys = pygame.key.get_pressed()

        # Move the player tank based on key presses
        player_tank.tank_moved = player_tank.move(keys)

        # Fire the bullet when the spacebar is pressed
        if keys[pygame.K_SPACE]:
            player_tank.fire()

        # Draw the player tank (with blinking logic)
        player_tank.draw(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()  # Update the screen

    pygame.quit()
