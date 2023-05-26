import pygame

class Stormhead(pygame.sprite.Sprite):

    def __int__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.current_image_index = 0
        # self.image = self.run_images[self.current_image_index]
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.last_frame_changed = 0
        self.animation_cooldown = 100





    def update(self, elapsed_time):
        # if elapsed_time - self.last_frame_changed > self.animation_cooldown:
        #     self.current_image_index += 1
        #     self.last_frame_changed = elapsed_time
        pass