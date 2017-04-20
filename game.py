
#Include pygame which we got from pip
import pygame

#In order to use pygame, we have to run the init method
pygame.init()

#Create a screen with a size
screen = {
	"height": 512,
	"width": 480
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10
}

screen_size = (screen["height"], screen["width"]) #Necessary for pygame
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase") #This shows up at the top of the window
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/princesspeach.png')

#Below are to rescale the image in python
#hero_image = pygame.image.load('./images/hero.png')
#hero_image_scaled = pygame.transform.scale(hero_image, (199,196));

#Create the game loop
#//////////////////////////////////////////////////////
#////////////////////MAIN GAME LOOP////////////////////
#//////////////////////////////////////////////////////
game_on = True
while game_on:
	#we are insite the main game loop. It will run as long as game_on is true
	#Add a quit event. Necessary for pygame to run
	# ---EVENTS!!---
	for event in pygame.event.get():
		#Looping through all events that happen this game loop cycle
		if event.type == pygame.QUIT:
			#The user clicked on the red X to leave the game
			game_on = False
			#Update our boolean so pygame can escape the loop
		elif event.type == pygame.KEYDOWN:
			#print event.key 	#This shows the number associated with the keys (put in key dictionary)
			if event.key == keys["up"]:
				#print "User pressed up!"
				keys_down["up"] = True
			elif event.key == keys["down"]:
				#print "User pressed down!"
				keys_down["down"] = True
			elif event.key == keys["right"]:
				#print "User pressed right!"
				keys_down["right"] = True
			elif event.key == keys["left"]:
				#print "User pressed left!"
				keys_down["left"] = True
		elif event.type == pygame.KEYUP:	#To address lifting up keystroke
			print "The user let go of a key"
			if event.key == keys["up"]:
				#the user let go of a key... and that key was the up arrow
				keys_down["up"] = False
			if event.key == keys["down"]:
				keys_down["down"] = False
			if event.key == keys["right"]:
				keys_down["right"] = False
			if event.key == keys["left"]:
				keys_down["left"] = False

	#Update hero position, happens every time regardless of user
	if keys_down["up"]:
		hero["y"] -= hero["speed"]
	elif keys_down["down"]:
		hero["y"] += hero["speed"]
	if keys_down["left"]:
		hero["x"] -= hero["speed"]
	elif keys_down["right"]:
		hero["x"] += hero["speed"]


	# ---RENDER!---
	#blit takes 2 arguments: [1. What?, 2. Where?]
	#to draw something on something else (drawing on screen)
	pygame_screen.blit(background_image, [0,0]) #starting point of image

	#draw the hero
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])

	#Flip the screen and start over: clear the screen for next time
	pygame.display.flip()

