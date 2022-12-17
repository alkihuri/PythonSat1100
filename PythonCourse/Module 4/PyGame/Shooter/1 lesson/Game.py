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
y = 1000
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
    screen.blit(player_surface,(x,y))

    #Player movements
    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5

    if keys[K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += 5

    if keys[K_UP] and player_rect.top > 0:
        player_rect.y -= 5

    if keys[K_DOWN] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.y += 5

    #updating the display
    pygame.display.update()
    clock.tick(144)