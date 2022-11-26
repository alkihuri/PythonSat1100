from time import *
import pygame.sprite
from pygame import *
import random
from os import path

width = 480
height = 600

# Create window
init()
mixer.init()
window = display.set_mode((width, height))
display.set_caption("Shooter")
Clock = time.Clock()

# GameSprites
background = image.load("img/starfield.jpg").convert()
background_rect = background.get_rect()
player_img = image.load("img/playerShip1_orange.png").convert()
player_img_rect = player_img.get_rect()
npc_img = image.load("img/rocket_3.png")
npc_img = transform.rotate(npc_img, 180)
bullet_img = image.load("img/laserRed16.png")


class Player(sprite.Sprite):
    score = 0

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(npc_img, (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-300, -30)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


all_sprites = sprite.Group()
Player = Player()
mobs = sprite.Group()
all_sprites.add(Player)
for i in range(2):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    Clock.tick(15)
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                print("shoot")

    all_sprites.update()
    window.fill((0, 0, 0))
    window.blit(background, background_rect)
    all_sprites.draw(window)
    display.flip()

quit()
