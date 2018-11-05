from time import sleep
import sys
import pygame
from pygame import key
from pygame.locals import *


def sign(x):
    """Returns the sign of the number given"""
    return 1 if x == abs(x) else -1

pygame.init()

size = width, height = 1280, 720   # window size
velocity_x = 1  # velocity in the x axis, for the physics
velocity_y = 0  # ditto for y
fps = 60  # target fps which determines general game speed
gravity = 1/2  # gravity constant
white = 255, 255, 255  # background color
bounciness = 0.01  # bounciness of the level floor
friction = 0.2  # friction of the level floor
last_touched = False  # temp variable
movements = {"left": False, "right": False, "up": False}  # keep track of whether we are moving and where
accel = 0.8  # character's acceleration
top_speed = 8  # character's top speed
jumps = 0
jump_limit = 2  # maximum number of jumps the character can make
jump_velocity = -12

screen = pygame.display.set_mode(size)

char = pygame.image.load("assets/pixelguy@2x.png")  # the character sprite
char_rect = char.get_rect()

background = pygame.image.load("assets/Background.png")

while 1:
    for event in pygame.event.get():  # event processing
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()  # handle window close
        if event.type == pygame.KEYDOWN:  # handle key press down
            k = event.key  # code of the key being pressed down
            if k == pygame.K_SPACE or k == pygame.K_UP:  # jump
                movements['up'] = True
            if k == pygame.K_LEFT:  # move left
                movements['left'] = True
            if k == pygame.K_RIGHT:  # move right
                movements['right'] = True
        if event.type == pygame.KEYUP:  # handle key release
            k = event.key  # code of the key being released
            if k == pygame.K_LEFT:  # stop moving left
                movements['left'] = False
            if k == pygame.K_RIGHT:  # stop moving right
                movements['right'] = False

    if char_rect.left < 0 or char_rect.right > width:
        char_rect = char_rect.move([-velocity_x, 0])  # get stopped by window sides

    if char_rect.top < 0:
        velocity_y = gravity  # fix getting stuck on top of the window
        char_rect = char_rect.move([0, -char_rect.top])  # fix flying above the window

    if True not in [movements['right'], movements['left']]:
        velocity_x -= velocity_x * friction  # apply friction if the player is not moving

    if char_rect.bottom > height:
#        char_rect.move([0, height-char_rect.bottom-15])  # fix underclipping
        if abs(velocity_y) > 0.5:
            print("Bounced: %f" % velocity_y)
        velocity_y = abs(velocity_y) * -bounciness
        #velocity_y = -1
        jumps = 0

    if movements['up'] and jumps < jump_limit:
        movements['up'] = False
        velocity_y = jump_velocity
        jumps += 1

    if movements['right']:
        if velocity_x >= top_speed:
            velocity_x = top_speed
        else:
            velocity_x += accel

    if movements['left']:
        if velocity_x <= -top_speed:
            velocity_x = -top_speed
        else:
            velocity_x -= accel

    velocity_y += gravity

    char_rect = char_rect.move([velocity_x, velocity_y])

    screen.fill(white)
    screen.blit(char, char_rect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)
