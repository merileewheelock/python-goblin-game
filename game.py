import pygame
from math import fabs
from random import randint
pygame.init()

# GLOBAL VARIABLES AND DICTIONARIES

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
	"speed": 1,
	"direction": "N"
}

directions = ['N','S','E','W','NE','NW','SE','SW']

monster = {
	"x": 200,
	"y": 200,
	"speed": 2
}

mushroom = {
	"x": 350,
	"y": 200,
	"active": True,
	"tick_gotten": 0
}


screen_size = (screen["width"], screen["height"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/mariobg.png')
hero_image = pygame.image.load('images/princesspeach.png')
star_image = pygame.image.load('images/star.png')
monster_image = pygame.image.load('images/bowser.png')
mushroom_image = pygame.image.load('images/mushroom.png')
pygame.mixer.music.load("./sounds/music.wav")
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound("sounds/mario_win.wav")
lose_sound = pygame.mixer.Sound("sounds/mario_loss.wav")

def main():

	tick = 0 
	timer = 0
	game_on = True
	while game_on:

		tick += 1

		#EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_on = False
			elif event.type == pygame.KEYDOWN:
				for keystroke in keys:
					if event.key == keys[keystroke]:
						keys_down[keystroke] = True
			elif event.type == pygame.KEYUP:
				for keystroke in keys:
					if event.key == keys[keystroke]:
						keys_down[keystroke] = False

		if keys_down["up"]:
			if hero["y"] > 0:
				hero["y"] -= hero["speed"]
		elif keys_down["down"]:
			if hero["y"] < screen["height"] - 65:
				hero["y"] += hero["speed"]
		if keys_down["left"]:
			if hero["x"] > 0:
				hero["x"] -= hero["speed"]
		elif keys_down["right"]:
			if hero["x"] < screen["width"] - 45:
				hero["x"] += hero["speed"]

		def movements():

			#MOVING STAR
			# for i in directions:
			# 	if star["direction"] == 

			if (star["direction"] == "N"):
				star['y'] -= star["speed"]
			elif (star["direction"] == "S"):
				star['y'] += star["speed"]
			elif (star["direction"] == "E"):
				star['x'] += star["speed"]
			elif (star["direction"] == "W"):
				star['x'] -= star["speed"]
			elif (star["direction"] == "NE"):
				star['y'] -= star["speed"]
				star['x'] += star["speed"]
			elif (star["direction"] == "NW"):
				star['y'] -= star["speed"]
				star['x'] -= star["speed"]
			elif (star["direction"] == "SE"):
				star['y'] += star["speed"]
				star['x'] += star["speed"]
			elif (star["direction"] == "SW"):
				star['y'] += star["speed"]
				star['x'] -= star["speed"]

			#KEEP STAR FROM MOVING TOO OFTEN
			if (tick % 20 == 0):
				new_dir_index = randint(0, len(directions) - 1)
				star["direction"] = directions[new_dir_index]

			#KEEP STAR ON SCREEN
			if (star['x'] > screen['width'] - 50):
				star['x'] = 1
			elif (star['x'] < 1):
				star['x'] = screen['width']
			if (star['y'] > screen['height'] - 50):
				star['y'] = 1
			elif (star['y'] < 1):
				star['y'] = screen['height']

			# MOVING MONSTER - CHASE HERO
			if monster['x'] > hero['x']:
				monster['x'] -= monster["speed"]
			elif monster['x'] < hero['x']:
				monster['x'] += monster["speed"]
			if monster['y'] > hero['y']:
				monster['y'] -= monster["speed"]
			elif monster['y'] < hero['y']:
				monster['y'] += monster["speed"]

		movements()

		def collision():

			# COLLISION DETECTION -- STAR
			distance_between_star = fabs(hero['x'] - star['x']) + fabs(hero['y'] - star['y'])
			if (distance_between_star < 50):
				rand_x = randint(25, screen["width"] - 100)
				rand_y = randint(25, screen["height"] - 100)
				star['x'] = rand_x
				star['y'] = rand_y
				hero["wins"] += 1
				star["speed"] += .3
				monster["speed"] += .3
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
				hero["speed"] = 20

		collision()


		#RENDER
		pygame_screen.blit(background_image, [0,0])
		font = pygame.font.Font(None, 25)
		wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
		losses_text = font.render("Losses: %d" % (hero['losses']), True, (0,0,0))

		if (tick % 60 == 0):
			timer += 1
		timer_text = font.render("Seconds Playing: %d" % (timer), True, (0,0,0))

		pygame_screen.blit(wins_text, [40,40])
		pygame_screen.blit(losses_text, [40, 60])
		pygame_screen.blit(timer_text, [40, 80])
		pygame_screen.blit(mushroom_image, [mushroom['x'], mushroom['y']])
		pygame_screen.blit(hero_image, [hero['x'], hero['y']])
		pygame_screen.blit(star_image, [star['x'], star['y']])
		pygame_screen.blit(monster_image, [monster['x'], monster['y']])
		pygame.display.flip()

main()