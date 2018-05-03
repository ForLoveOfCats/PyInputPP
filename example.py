'''This is the example file for the PyInput++ library.

All comments are on lines of importance when learning how to use PyInput++.
Any line without a comment can be assumed to be stock standard code when working with pygame.'''

import pygame
import inpp  # Import PyInput++ (ensure inpp.py is in the same directory as the file importing it)


SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
PLAYER_SIZE = 50

pygame.init()
window = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HIGHT) )
pygame.display.set_caption('PyInput++ Example')

clock = pygame.time.Clock()

controller = inpp.Controller()  # Create a inpp controller object. All of the library's functionaly is within this class.

player_pos = [int(SCREEN_WIDTH/2)-int(PLAYER_SIZE/2),0]
player_vel = [0,0]

def tick_physics():
	global player_pos, player_vel

	player_vel[1] += 1

	if player_vel[0] > 0:
		player_vel[0] -= 1
	elif player_vel[0] < 0:
		player_vel[0] += 1

	player_pos = [player_pos[0]+player_vel[0], player_pos[1]+player_vel[1]]

	if player_pos[1] > SCREEN_HIGHT-PLAYER_SIZE:
		player_pos[1] = SCREEN_HIGHT-PLAYER_SIZE
		player_vel[1] = 0

	if player_pos[0] > SCREEN_WIDTH-PLAYER_SIZE:
		player_pos[0] = SCREEN_WIDTH-PLAYER_SIZE
		player_vel[0] = 0
	elif player_pos[0] < 0:
		player_pos[0] = 0
		player_vel[0] = 0

while True:
	window.fill( (255,255,255) )
	controller.update()  # Run controller update logic. Run this once per frame before any frame logic.

	if controller.events.quit() or controller.events.key(pygame.K_ESCAPE):  # Check to see if events.quit() returns True or if the Escape key fired.
		break

	if controller.events.key(pygame.K_w) or controller.events.mouse('Left'):  # Check if the W key or the Left mouse button fired.
		player_vel[1] = -22

	if controller.repeats.key(pygame.K_a):  # Check if the A key fired.
		player_vel[0] -= 2

	if controller.events.scroll('Up'):  # Check if the mouse wheel scrolled up.
		if player_vel[0] > 0:
			player_vel[0] = 0
		player_vel[0] -= 10

	if controller.repeats.key(pygame.K_d):  # Check if the D key fired.
		player_vel[0] += 2

	if controller.events.scroll('Down'):  # Check if the mouse wheel scrolled down.
		if player_vel[0] < 0:
			player_vel[0] = 0
		player_vel[0] += 10

	tick_physics()
	pygame.draw.rect(window, (0,0,0), [player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE])

	pygame.display.update()
	clock.tick_busy_loop(60)
