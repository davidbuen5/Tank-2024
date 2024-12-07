import pygame
from game_assets import bullets

bullet_img = bullets()

pygame.init()

class Bullet:
    def __init__(self, x, y, direction, speed=0.2):
        self.x = x
        self.y = y
        self.direction = direction  # Direction of the bullet ('UP', 'DOWN', 'LEFT', 'RIGHT')
        self.speed = speed
        self.width = 10  # Bullet width
        self.height = 10  # Bullet height
        self.image = bullet_img  # Bullet image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Rect for collision detection

        # Rotate the image based on the direction
        self.image = self.rotate_image(self.image, self.direction)

    def rotate_image(self, image, direction):
        """Rotate the bullet image based on the given direction."""
        if direction == 'UP':
            return pygame.transform.rotate(image, 0)  # No rotation for UP
        elif direction == 'DOWN':
            return pygame.transform.rotate(image, 180)  # Rotate 180 degrees for DOWN
        elif direction == 'LEFT':
            return pygame.transform.rotate(image, 90)  # Rotate 90 degrees for LEFT
        elif direction == 'RIGHT':
            return pygame.transform.rotate(image, -90)  # Rotate -90 degrees for RIGHT

    def move(self):
        """Move the bullet in the direction of the tank."""
        if self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
        elif self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed

        # Update the bullet's rectangle position
        self.rect.x = self.x
        self.rect.y = self.y

    def check_collision(self, player_tank, enemy_tanks, walls, eagle, stones):
        """Check for collisions with the player, enemies, walls, eagle, and stones."""
        
        # Collision with the player tank (bullet and tank disappear)
        if self.rect.colliderect(player_tank.rect):
            player_tank.destroy()  # Call destroy method to remove the player tank
            self.destroy()  # Destroy the bullet
        
        # Collision with enemy tanks (bullet and enemy disappear)
        for enemy in enemy_tanks:
            if self.rect.colliderect(enemy.rect):
                enemy.destroy()  # Call destroy method to remove the enemy
                self.destroy()  # Destroy the bullet

        # Collision with walls (bullet and wall disappear)
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                wall.destroy()  # Call destroy method to remove the wall
                self.destroy()  # Destroy the bullet
        
        # Collision with the eagle (bullet and eagle disappear)
        if self.rect.colliderect(eagle.rect):
            eagle.destroy()  # Call destroy method to remove the eagle
            self.destroy()  # Destroy the bullet
        
        # Collision with stones (bullet disappears, but stone stays)
        for stone in stones:
            if self.rect.colliderect(stone.rect):
                self.destroy()  # Destroy the bullet

    def destroy(self):
        """Method to destroy the bullet."""
        self.x = -999  # Move the bullet off-screen
        self.y = -999
        self.rect.x = -999
        self.rect.y = -999

    def draw(self, screen):
        """Draw the bullet on the screen."""
        screen.blit(self.image, (self.x, self.y))

# Example of how to use the Bullet class:

# Initialize screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bullet Demo")

# Create an instance of Bullet
player_bullet = Bullet(400, 300, 'UP')  # Starting at position (400, 300) and moving upwards

# Dummy objects for testing collision (you should replace these with your actual game objects)
class DummyObject:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)  # Dummy rectangle for collision

    def destroy(self):
        pass  # Replace with logic to destroy the object

player_tank = DummyObject(400, 250)
enemy_tanks = [DummyObject(300, 300), DummyObject(500, 300)]
walls = [DummyObject(200, 200), DummyObject(600, 200)]
eagle = DummyObject(400, 100)
stones = [DummyObject(350, 350), DummyObject(450, 350)]

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    # Move and draw the bullet
    player_bullet.move()
    player_bullet.draw(screen)

    # Check for collisions
    player_bullet.check_collision(player_tank, enemy_tanks, walls, eagle, stones)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Update the screen

pygame.quit()
