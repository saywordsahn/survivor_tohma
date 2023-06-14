import pygame
import random
from spritesheet import Spritesheet

class Stormhead(pygame.sprite.Sprite):

    def __init__(self):
        ss = Spritesheet('stormhead/run.png')
        pygame.sprite.Sprite.__init__(self)
        self.images = ss.load_strip_vert((0, 0, 119, 124), 10, -1)
        self.frame_counter = random.randint(0, len(self.images) - 1)
        self.image = self.images[self.frame_counter]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 100)
        self.animation_cooldown = 70
        self.last_frame_change = -self.animation_cooldown
        self.speed = 1


    def update(self, elapsed_time):
        if elapsed_time - self.last_frame_change > self.animation_cooldown:
            # switch frame
            self.image = self.images[self.frame_counter % len(self.images)]
            self.last_frame_change = elapsed_time
            self.frame_counter += 1
