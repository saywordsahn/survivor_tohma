import pygame
from spritesheet import Spritesheet

class Stormhead(pygame.sprite.Sprite):

    def __init__(self):
        ss = Spritesheet('stormhead/run.png')
        pygame.sprite.Sprite.__init__(self)
        self.images = ss.load_strip_vert((0, 0, 119, 124), 10, -1)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 100)