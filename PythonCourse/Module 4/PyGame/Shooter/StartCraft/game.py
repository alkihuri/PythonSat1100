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
background = image.load("img/starfield.png").convert()
background_rect = background.get_rect()
player_img = image.load("img/playerShip1_orange.png").convert()
player_img_rect = player_img.get_rect()
npc_img = image.load("img/meteorBrown_med1.png")
bullet_img = image.load("img/laserRed16.png")


class Player(sprite.Sprite):
    score = 0

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale("img/playerShip1_orange.png", (50, 50))
        self.image.set_colorkey(255, 255, 255)
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


running = True
while running:
    Clock.tick(15)
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                print("shoot")

    sprite.Group().update()
    window.fill((0, 0, 0))
    window.blit(background, background_rect)
    sprite.Group().draw(window)
    display.flip()

quit()
