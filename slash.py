import pygame

class Slash(pygame.sprite.Sprite):

    def __init__(self, images, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.current_image = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_image += 1

        if self.current_image >= len(self.images):
            self.kill()
            return

        self.image = self.images[self.current_image % len(self.images)]