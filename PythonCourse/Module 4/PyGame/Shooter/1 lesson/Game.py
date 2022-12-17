
# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85

# modules import 
import pygame

# colors set up
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Window creating
window = display.set_mode((700, 500))
display.set_caption("First application")
window.fill((red))
 
# Game sprites 
height = 60
width = 40
xCoord = 100
yCoord = 100



#player class
draw.rect(window, (a, b, c), (xCoord, yCoord, width, height))
display.update()
time.delay(5000)
run = True
while run:
    time.delay(50)
    
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K.LEFT:
                xCoord - 1
            if e.key == K.RIGHT:
                xCoord + 1
            if e.key == K.UP:
                yCoord + 1
            if e.key == K.DOWN:
                yCoord - 1   

#mob class
enemies = sprite.Group()
for i in range (1, 6):
    monster = Enemy()
    monsters.add(monster)
    monsters.update()
    monsters.draw(window)

#bullet class
if self.rect.y < 0:
    self.kill()
    
    collides = sprite.groupcollide(monsters, bullets, True, True)#
for c in collides:
    monster = Enemy()
    monsters.add(monsters)
#Game entities innit

# Game Lifecycle

# rendering
backGround = image.load("player.png")

#win lose  situation 
    
#text 
font.init()
font = font.Font(None, 36)
text = font.render ("Score: " + str(score), 1, (255, 255, 255))
window.blit(text, (10, 20))

 