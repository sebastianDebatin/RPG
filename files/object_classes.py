"""
This file defines all gameobjects like units, buttons...

"""
import pygame
import pytmx
import os



class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posx = 0
        self.posy = 0
        self.velocity = 16

        self.move_up_sprites = []
        dirname = r"files\assets\char\move_up"
        for sprite in os.listdir(os.path.normpath(dirname)):
            self.move_up_sprites.append(pygame.image.load(os.path.join(dirname, sprite)).convert_alpha())

        self.move_right_sprites = []
        dirname = r"files\assets\char\move_right"
        for sprite in os.listdir(os.path.normpath(dirname)):
            self.move_right_sprites.append(pygame.image.load(os.path.join(dirname, sprite)).convert_alpha())

        self.move_left_sprites = []
        dirname = r"files\assets\char\move_left"
        for sprite in os.listdir(os.path.normpath(dirname)):
            self.move_left_sprites.append(pygame.image.load(os.path.join(dirname, sprite)).convert_alpha())

        self.move_down_sprites = []
        dirname = r"files\assets\char\move_down"
        for sprite in os.listdir(os.path.normpath(dirname)):
            self.move_down_sprites.append(pygame.image.load(os.path.join(dirname, sprite)).convert_alpha())
                               


    def move_left(self): # todo: find out how WIDTH and HEIGHT can be sent to this class without heving to create a gamsetate object
        if self.posx > 0 + self.velocity:
            self.posx -= self.velocity

    def move_right(self):
        if self.posx < 800 - self.velocity:
            self.posx += self.velocity

    def move_up(self):
        if self.posy > 0 + self.velocity:
            self.posy -= self.velocity

    def move_down(self):
        if self.posy < 800 - self.velocity:
            self.posy += self.velocity


class button(pygame.sprite.Sprite):
    def __init__(self):
        pass