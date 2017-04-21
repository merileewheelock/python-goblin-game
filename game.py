
#Include pygame which we got from pip
import pygame

#bring in the math module so we can use absolute value
from math import fabs

#get the random module
from random import randint

#In order to use pygame, we have to run the init method
pygame.init()

#Create a screen with a size
screen = {
	"height": 500,
	"width": 800
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
	"speed": 10,
	"wins": 0,
	"losses": 0
}

star = {
	"x": 300,
	"y": 300,
	"speed": 10
}

monster = {
	"x": 200,
	"y": 200,
	"speed": 10
}

mushroom = {
	"x": 350,
	"y": 200
}

screen_size = (screen["width"], screen["height"]) #Necessary for pygame
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase") #This shows up at the top of the window
background_image = pygame.image.load('images/mariobg.png')
hero_image = pygame.image.load('images/princesspeach.png')
star_image = pygame.image.load('images/star.png')
monster_image = pygame.image.load('images/bowser.png')
mushroom_image = pygame.image.load('images/mushroom.png')

#Add music files
pygame.mixer.music.load("sounds/music.wav")
#Play music below
pygame.mixer.music.play(-1) #-1 will play indefinitely
win_sound = pygame.mixer.Sound("sounds/mario_win.wav")
lose_sound = pygame.mixer.Sound("sounds/mario_loss.wav")

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
			#print "The user let go of a key"
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
		if hero["y"] > 0:	#Keeps player inside screen
			hero["y"] -= hero["speed"]
	elif keys_down["down"]:
		if hero["y"] < screen["height"] - 60:
			hero["y"] += hero["speed"]
	if keys_down["left"]:
		if hero["x"] > 0:
			hero["x"] -= hero["speed"]
	elif keys_down["right"]:
		if hero["x"] < screen["width"] - 40:
			hero["x"] += hero["speed"]



	# COLLISION DETECTION -- STAR
	distance_between_star = fabs(hero['x'] - star['x']) + fabs(hero['y'] - star['y'])
	#need absolute value since the hero could be coming from right/left or up/down
	if (distance_between_star < 50): #32 pixels based on scale of image
		#the hero and star are touching!
		#print ("Collision!!")
		#Generate a random X > 0, X < screen["width"]
		#Generate a random Y > 0, Y < screen["height"]
		rand_x = randint(25, screen["width"] - 100)
		rand_y = randint(25, screen["height"] - 100)
		star['x'] = rand_x
		star['y'] = rand_y
		#Update the hero's wins
		hero["wins"] += 1
		win_sound.play()


	# COLLISION DETECTION -- MONSTER (BOSWER)
	distance_between_monster = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if (distance_between_monster < 50):
		rand_x = randint(0, screen["width"] - 50)
		rand_y = randint(0, screen["height"] - 50)
		monster['x'] = rand_x
		monster['y'] = rand_y
		hero["losses"] += 1
		lose_sound.play()

	# COLLISION DETECTION -- MUSHROOM
	distance_between_mushroom = fabs(hero['x'] - mushroom['x']) + fabs(hero['y'] - mushroom['y'])
	if (distance_between_mushroom < 50):
		hero["speed"] = 30
		#Need a timer on this power up


	# MOVING MONSTER
	monster_location = randint(1,4)
	if monster_location == 1:
		monster['x'] += 5 #Move right
	if monster_location == 2:
		monster['x'] -= 5 #Move left
	if monster_location == 3:
		monster['y'] += 5 #Move up
	if monster_location == 4:
		monster['y'] -= 5 #Move down


	# ---RENDER!---
	#blit takes 2 arguments: [1. What?, 2. Where?]
	#to draw something on something else (drawing on screen)
	pygame_screen.blit(background_image, [0,0]) #starting point of image

	#Draw the hero wins text on the screen
	font = pygame.font.Font(None, 25) #1st is special font, 2nd is pixels for font
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	losses_text = font.render("Losses: %d" % (hero['losses']), True, (0,0,0))
	#render needs extra parameters
	#True: Tells whether font should have smooth edges; false would be pixelated text
	#(0,0,0) is RGB
	pygame_screen.blit(wins_text, [40,40])
	pygame_screen.blit(losses_text, [40, 60])

	pygame_screen.blit(mushroom_image, [mushroom['x'], mushroom['y']])

	#draw the hero
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame_screen.blit(star_image, [star['x'], star['y']])

	pygame_screen.blit(monster_image, [monster['x'], monster['y']])


	#Flip the screen and start over: clear the screen for next time
	pygame.display.flip()

