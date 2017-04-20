
#Include pygame which we got from pip
import pygame

#In order to use pygame, we have to run the init method
pygame.init()

#Create a screen with a size
screen = {
	"height": 512,
	"width": 480
}

screen_size = (screen["height"], screen["width"]) #Necessary for pygame
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase") #This shows up at the top of the window

#Create the game loop (while 1)
game_on = True
while game_on:
	#we are insite the main game loop. It will run as long as game_on is true
	#Add a quit event. Necessary for pygame to run
	for event in pygame.event.get():
		#Looping through all events that happen this game loop cycle
		if event.type == pygame.QUIT:
			#The user clicked on the red X to leave the game
			game_on = False
			#Update our boolean so pygame can escape the loop


