"""Game"""


from time import sleep
import sys
import pygame
from pygame import *
from pygame.locals import *
from enum import Enum

# Marcus was here


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Object(sprite.Sprite):
    def __init__(self, groups, xpos, ypos, img):
        super().__init__(groups)
        self.xpos = xpos
        self.ypos = ypos
        self.image = img
        self.rect = self.img.get_rect()
        self.xvel = 0
        self.yvel = 0

    def tick(self):
        """Ticks the object"""
        self.rect = self.rect.move([self.xvel, self.yvel])


class Player(Object):
    def __init__(self, groups, img, accel, friction, top_speed, jump_limit, jump_velocity)
        super().__init__(groups, 0, 0, img)
        self.accel = accel
        self.friction = friction
        self.top_speed = top_speed
        self.jump_limit = jump_limit
        self.jump_velocity = jump_velocity
        self.jumps = 0
        self.movements = {"left": False, "right": False, "up": False}  # keep track of whether we are moving and where

    def tick(self):
        # ...
        if True not in [self.movements['right'], self.movements['left']]:
            xvel -= xvel * friction  # apply friction if the player is not moving

        if self.movements['up'] and self.jumps < self.jump_limit:
            self.movements['up'] = False
            self.yvel = self.jump_velocity
            self.jumps += 1

        if self.movements['right']:
            if self.xvel >= self.top_speed:
                self.xvel = self.top_speed
            else:
                self.xvel += self.accel

        if self.movements['left']:
            if self.xvel <= -self.top_speed:
                self.xvel = -self.top_speed
            else:
                self.xvel -= self.accel

        self.yvel += gravity
        super().tick()


def sign(value):
    """Returns the sign of the number given"""
    return 1 if value == abs(value) else -1


def main():
    """Runs the game main loop"""
    pygame.init()

    size = width, height = 900, 600   # window size
    fps = 120  # target fps which determines general game speed
    gravity = 3/4  # gravity constant
    white = 255, 255, 255  # background color
    bounciness = 0  # bounciness of the level floor
    friction = 0.2  # friction of the level floor

    screen = pygame.display.set_mode(size)

    players = sprite.RenderClear()

    char = Player(
        groups = players,
        img = pygame.image.load("assets/pixelguy@2x.png"),  # the character sprite
        accel = 1,
        top_speed = 8,
        jump_limit = 2,
        jump_velocity = -12
    )

    background = pygame.image.load("assets/Background@6x.png")

    while True:
        for game_event in pygame.event.get():  # event processing
            print(game_event)
            if game_event.type == QUIT:
                sys.exit()  # handle window close
            if game_event.type == KEYDOWN:  # handle key press down
                k = game_event.key  # code of the key being pressed down
                if k == K_SPACE or k == K_UP:  # jump
                    movements['up'] = True
                if k == K_LEFT:  # move left
                    movements['left'] = True
                if k == K_RIGHT:  # move right
                    movements['right'] = True
            if game_event.type == KEYUP:  # handle key release
                k = game_event.key  # code of the key being released
                if k == K_LEFT:  # stop moving left
                    movements['left'] = False
                if k == K_RIGHT:  # stop moving right
                    movements['right'] = False

        if char_rect.left < 0 or char_rect.right > width:
            char_rect = char_rect.move([-velocity_x, 0])  # get stopped by window sides

        if char_rect.top < 0:
            velocity_y = gravity  # fix getting stuck on top of the window
            char_rect = char_rect.move([0, -char_rect.top])  # fix flying above the window


        if char_rect.bottom > height:
            if abs(velocity_y) > 0.5:
                print("Bounced: %f" % velocity_y)
            velocity_y = abs(velocity_y) * -bounciness
            # velocity_y = -1
            jumps = 0

        screen.fill(white)
        screen.blit(background, (0, 0))
        pygame.display.flip()

#        pygame.time.Clock().tick(fps)
        sleep(1/fps)


if __name__ == "__main__":
    main()
