import pygame

# Walls
brick_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\walls\\1.png"
stone_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\walls\\2.png"

# Eagle
eagle1_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\eagle\\eagle1.png"
eagle2_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\eagle\\eagle2.png"
eagle3_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\eagle\\eagle3.png"
eagle4_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\eagle\\eagle4.png"
eagle5_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\eagle\\eagle.png"

# Tank
tankDown = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\hero1D.png"
tankUp = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\hero1U.png"
tankLeft = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\hero1L.png"
tankRight = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\hero1R.png"
blink1_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\blink1.png"
blink2_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\hero\\blink2.png"

# Enemy
enemy1D_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\enemy\\enemy1D.png"
enemy1U_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\enemy\\enemy1U.png"
enemy1L_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\enemy\\enemy1L.png"
enemy1R_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\enemy\\enemy1R.png"

# Bullet
bullet = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\bullet\\bullet.png"

# Fire sound
fire_sound_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\musics\\fire.wav"

# Explotion sound
explosion_sound_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\musics\\boom.wav"

# Power Ups
bonus_gun_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\power_ups\\bonus_gun.png"
bonus_tank_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\power_ups\\bonus_grenade.png"
bonus_star_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\power_ups\\bonus_star.png"
bonus_stone_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\power_ups\\bonus_helmet.png"

# Blast
blast1_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast1.png"
blast2_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast2.png"
blast3_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast3.png"
blast4_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast4.png"
blast5_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast5.png"
blast6_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast6.png"
blast7_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast7.png"
blast8_path = "C:\\Users\\Nichols\\Documents\\PYGAME PROJECT\\Pygame Level\\images\\boom\\blast8.png"

def walls():
    brick = pygame.image.load(brick_path)
    stone = pygame.image.load(stone_path)
    
    # Scale the images to the desired tile size
    brick = pygame.transform.scale(brick, (32, 32))
    stone = pygame.transform.scale(stone, (32, 32))
    
    return brick, stone

def eagle():
    eagle1 = pygame.image.load(eagle1_path)
    eagle2 = pygame.image.load(eagle2_path)
    eagle3 = pygame.image.load(eagle3_path)
    eagle4 = pygame.image.load(eagle4_path)
    eagle5 = pygame.image.load(eagle5_path)

    eagle5 = pygame.transform.scale(eagle5, (32, 32))

    eagle1 = pygame.transform.scale(eagle1, (32, 32))
    eagle2 = pygame.transform.scale(eagle2, (32, 32))
    eagle3 = pygame.transform.scale(eagle3, (32, 32))
    eagle4 = pygame.transform.scale(eagle4, (32, 32))

    return eagle1, eagle2, eagle3, eagle4, eagle5

def tank():
    tankD = pygame.image.load(tankDown)
    tankU = pygame.image.load(tankUp)
    tankL = pygame.image.load(tankLeft)
    tankR = pygame.image.load(tankRight)
    blink1 = pygame.image.load(blink1_path)
    blink2 = pygame.image.load(blink2_path)

    tankD = pygame.transform.scale(tankD, (20, 20))
    tankU = pygame.transform.scale(tankU, (20, 20))
    tankL = pygame.transform.scale(tankL, (20, 20))
    tankR = pygame.transform.scale(tankR, (20, 20))
    blink1 = pygame.transform.scale(blink1, (20, 20))
    blink2 = pygame.transform.scale(blink2, (20, 20))

    return tankD, tankU, tankL, tankR, blink2, blink1

def bullets():
    bullet_img = pygame.image.load(bullet)

    bullet_img = pygame.transform.scale(bullet_img, (5,5))

    return bullet_img

def fire():
    fire_sound = pygame.mixer.Sound(fire_sound_path)

    return fire_sound

def explosion():
    explosion_sound = pygame.mixer.Sound(explosion_sound_path)

    return explosion_sound

def blast():
    blast1 = pygame.image.load(blast1_path)
    blast2 = pygame.image.load(blast2_path)
    blast3 = pygame.image.load(blast3_path)
    blast4 = pygame.image.load(blast4_path)
    blast5 = pygame.image.load(blast5_path)
    blast6 = pygame.image.load(blast6_path)
    blast7 = pygame.image.load(blast7_path)
    blast8 = pygame.image.load(blast8_path)

    blast1 = pygame.transform.scale(blast1, (40, 40))
    blast2 = pygame.transform.scale(blast2, (40, 40))
    blast3 = pygame.transform.scale(blast3, (40, 40))
    blast4 = pygame.transform.scale(blast4, (40, 40))
    blast5 = pygame.transform.scale(blast5, (40, 40))
    blast6 = pygame.transform.scale(blast6, (40, 40))
    blast7 = pygame.transform.scale(blast7, (40, 40))
    blast8 = pygame.transform.scale(blast8, (40, 40))

    return blast1, blast2, blast3, blast4, blast5, blast6, blast7, blast8

def enemy():
    enemy1D = pygame.image.load(enemy1D_path)
    enemy1U = pygame.image.load(enemy1U_path)
    enemy1R = pygame.image.load(enemy1R_path)
    enemy1L = pygame.image.load(enemy1L_path)

    enemy1D = pygame.transform.scale(enemy1D, (50, 50))
    enemy1U = pygame.transform.scale(enemy1U, (50, 50))
    enemy1R = pygame.transform.scale(enemy1R, (50, 50))
    enemy1L = pygame.transform.scale(enemy1L, (50, 50))

    return enemy1D, enemy1U, enemy1R, enemy1L

def bonus():
    bonusgun = pygame.image.load(bonus_gun_path)
    bonustank = pygame.image.load(bonus_tank_path)
    bonusstar = pygame.image.load(bonus_star_path)
    bonusstone = pygame.image.load(bonus_stone_path)

    bonusgun = pygame.transform.scale(bonusgun, (32, 32))
    bonustank = pygame.transform.scale(bonustank, (32, 32))
    bonusstar = pygame.transform.scale(bonusstar, (32, 32))
    bonusstone = pygame.transform.scale(bonusstone, (32, 32))

    return bonusgun, bonustank, bonusstar, bonusstone