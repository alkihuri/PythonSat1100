print("Robolab Python Pro Course / Shooter template project =) ")

import pygame

#Window
pygame.init()
screen = pygame.display.set_mode((1920,1200))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

#adding text to the game
font = pygame.font.Font(None, 50)

#Surfaces
background_surface = pygame.image.load('city_2.png')
player_surface = pygame.image.load('ship.png')
text_surface = font.render("Testre", False, "Green")

x = 960
done = False
#While loop
while not done:
    # For loop to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #adding the surface
    screen.blit(background_surface,(-20,-150))
    screen.blit(text_surface,(100,200))
    screen.blit(player_surface,(x,1000))

    #Player movements
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x = x+15
            if event.key == pygame.K_a:
                x = x-15
            if event.key == pygame.K_r:
                x= 960

    #updating the display
    pygame.display.update()
    clock.tick(144)