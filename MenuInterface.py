# main_menu.py (or wherever the level menu is located)
import pygame
import sys
import os
import Level1Map  # Import the Level1Map script here

# Initialize Pygame
pygame.init()

# Screen dimensions
TILE_SIZE = 32

map_layout = [
    [' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    [' ', ' ', ' ', 'S', ' ', ' ', 'B', 'B', 'S', ' ', 'B', 'B', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'],
    ['S', 'S', ' ', 'S', 'S', ' ', 'S', 'S', 'S', 'S', 'S', 'B', 'S', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', ' ', ' ', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'S', ' ', 'S', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', ' ', 'S', 'S', 'S', 'B', 'S', ' ', 'S', 'S', 'S', ' ', 'S', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', 'S', 'B', ' ', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', ' ', 'S', 'S', 'S', ' ', 'S', ' ', 'S', ' ', 'S', 'B', 'S', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', ' ', 'S', 'B', 'S', ' ', ' ', ' ', 'S', ' ', 'S', 'B', 'S', 'S', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', 'B', 'S', 'B', 'S', ' ', 'B', 'B', 'S', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', 'B', ' ', ' ', 'S', ' ', 'B', 'B', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S'],
    ['S', 'B', 'S', 'S', 'S', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'],
    ['S', 'B', 'S', 'B', 'B', ' ', 'S', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'S', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'],
    ['S', 'S', 'S', 'S', 'B', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'S', ' ', 'S', ' ', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'S'],
    ['S', 'S', ' ', ' ', 'B', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', 'S', 'S', 'B', 'B', 'B', 'B', ' ', ' ', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'S', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'S', 'S', ' ', 'S', 'S', 'S', ' ', ' ', ' ', ' ', ' ', 'S'],
    ['S', ' ', 'B', 'B', 'S', ' ', 'S', 'B', ' ', ' ', 'B', 'B', 'B', 'B', 'B', 'S', ' ', ' ', ' ', ' ', ' ', 'S', 'S', 'S', ' ', 'S'],
    ['S', ' ', 'B', 'S', 'S', ' ', 'S', 'B', ' ', ' ', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', ' ', 'S'],
    ['S', ' ', 'B', 'S', 'B', ' ', 'S', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'B', 'B', 'B', 'B', 'S', ' ', ' ', ' ', 'S'],
    ['S', ' ', 'B', 'S', 'S', ' ', 'S', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', 'S', ' ', 'S', 'S', 'S'],
    ['S', ' ', 'B', 'B', ' ', ' ', 'S', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', 'S', ' ', 'S', 'S', 'S'],
    ['S', ' ', 'B', 'B', ' ', ' ', 'S', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', 'S'],
    ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', 'S', 'S', 'E5', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
]


SCREEN_WIDTH = len(map_layout[0]) * TILE_SIZE
SCREEN_HEIGHT = len(map_layout) * TILE_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (43, 43, 43)  # Background color #2b2b2b
START_GRADIENT_START = (255, 203, 61)  # #ffcb3d
START_GRADIENT_END = (255, 208, 0)  # #ffd000
QUIT_GRADIENT_START = (222, 58, 33)  # #de3a21
QUIT_GRADIENT_END = (194, 54, 54)  # #c23636
LEVEL_BUTTON_START = (120, 255, 120)
LOCKED_COLOR = (150, 150, 150)  # Gray for locked levels
TITLE_COLOR = (194, 54, 54)  # #c23636

# Font paths
TANK_FONT_PATH = os.path.join("font", "tank_font.ttf")
PRSTARTK_FONT_PATH = os.path.join("font", "prstartk.ttf")
LEVEL_FONT_PATH = os.path.join("font", "arialbd.ttf")

# Fonts
title_font = pygame.font.Font(TANK_FONT_PATH, 50)
button_font = pygame.font.Font(PRSTARTK_FONT_PATH, 40)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank 2024")

# Function to draw text
def draw_text(text, font, color, surface, x, y, align_center=True):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y) if align_center else (x, y))
    surface.blit(text_obj, text_rect)

# Function to draw a gradient rectangle
def draw_gradient_rect(surface, rect, start_color, end_color):
    x, y, width, height = rect
    for i in range(height):
        blend_ratio = i / height
        r = start_color[0] + (end_color[0] - start_color[0]) * blend_ratio
        g = start_color[1] + (end_color[1] - start_color[1]) * blend_ratio
        b = start_color[2] + (end_color[2] - start_color[2]) * blend_ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (x, y + i), (x + width, y + i))

# Button class
class Button:
    def __init__(self, text, x, y, width, height, gradient_start=None, gradient_end=None, is_locked=False):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_locked = is_locked
        self.gradient_start = gradient_start or LEVEL_BUTTON_START
        self.gradient_end = gradient_end or LEVEL_BUTTON_START
        self.color = LOCKED_COLOR if is_locked else None
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        if self.is_locked:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
            draw_text(self.text, button_font, WHITE, surface, self.x + self.width // 2, self.y + self.height // 2)
        else:
            draw_gradient_rect(surface, self.rect, self.gradient_start, self.gradient_end)
            draw_text(self.text, button_font, BLACK, surface, self.x + self.width // 2, self.y + self.height // 2)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.is_locked

# Calculate positions dynamically
title_x = SCREEN_WIDTH // 2
title_y = SCREEN_HEIGHT // 3 - 100

# Main menu
def main_menu():
    button_width = 300
    button_height = 100
    button_spacing = 20

    start_button = Button("Start", SCREEN_WIDTH // 2 - button_width // 2,
                          SCREEN_HEIGHT // 2 - button_height - button_spacing // 2,
                          button_width, button_height, START_GRADIENT_START, START_GRADIENT_END)
    quit_button = Button("Quit", SCREEN_WIDTH // 2 - button_width // 2,
                         SCREEN_HEIGHT // 2 + button_spacing // 2,
                         button_width, button_height, QUIT_GRADIENT_START, QUIT_GRADIENT_END)

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_text("Tank 2024", title_font, TITLE_COLOR, screen, title_x, title_y)

        start_button.draw(screen)
        quit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_button.is_clicked():
            Level1Map.start()
            running = False

        if quit_button.is_clicked():
            pygame.quit()
            sys.exit()

        pygame.display.update()

# Run the program
if __name__ == "__main__":
    main_menu()
