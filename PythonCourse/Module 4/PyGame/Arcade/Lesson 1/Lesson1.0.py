# Подключить нужные модули
from random import randint 
import pygame 
from os import path
pygame.init() 
# during the game we write inscriptions of size 72
 

#Global variables (settings)


# Colour:


# Classes
# class for the target (costs and does nothing)

    # class constructor
   
        # Call the class constructor (Sprite):
       

        # each sprite must store an image property - an image

        # each sprite must store the property of the rectum in which it is inscribed

#class for the main character
 
          # the picture is loaded from a file and fits in the muscles of the required size:
         
                      # often convert_alpha, we need to increase glucose levels

          # each sprite must store the square muscle property. This property is needed to detect sprite touches.
        
          # put the character at the given point (x, y):
         
          # create properties, remember passed values:
         
          # add property stand_on - this is the platform on which the character stands
        
          # if none, then the value is False
      #fall function (gravity)


      #function for jumping

      #update function for this sprite. because the sprite will move. the funniest part)
     

#class for walls. They did exactly the same in the Labyrinth project :)))
      #constructor

#enemy class
      #constructor

      # update function with random shift


# Run the game


# list of game features:


# list of events:

# list of enemies:

# list of mines:


# create a character, load it into a list of all sprites:

# create walls by building them:




# create opponents against them:


# create mines, consume them:
            
              # bombs are not collected in the list of all sprites, we will draw their separate commands
              # it's so easy to detonate bombs, and also make them stationary, update() does not rise

# create the final sprite, use it:

# Main game loop:
 
      # Event handling
      
          # Moving game objects

          # further check the rules of the game
          # check touch with bombs:
                  # if a bomb touches a sprite, then it is removed from the list of bombs, and the sprite is removed from all_sprites!

          # check touch by enemies:
             # robin.kill() # the kill method removes the sprite from all groups it belongs to

          # check screen borders:
               # at the end to the left or right, transfer the change to the outcome of the screen
              # moving on the way back all the sprites (and separately the bombs, they are in another list):
                          # robin himself is also in this list, so his switching move will be canceled
            

          # Rendering
          # draw the background with the rest
        

          # draw all sprites on the screen surface before checking for win/loss
          # if in this iteration of the loop the game ended, then a new background was drawn on top of the phenomena
         
          # draw a group of bombs separately - this way a bomb that has left its group will automatically cease to be visible
       

          # check for win and loss:
        

          # check for loss:
         
              # write text on the screen
             

     

      # Pause