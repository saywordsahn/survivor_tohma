import pygame
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet('Char_3.png')

        # load images
        self.idle_image = ss.image_at((0, 0, 64, 64, ))
        self.flying_image = ss.image_at((64 * 2, 64 * 1, 64, 64 ))
        self.walking_image = ss.image_at((64,64,64,64))

        self.electricity_images = ss.load_strip((64*0, 64*6, 64, 64), 4, (0, 0, 0))

        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.topright = (300, 300)

        self.player_walk_speed = 3
        self.player_flying_speed = 8
        self.player_speed = self.player_walk_speed
        self.in_flying_mode = False
        self.in_walking_mode = False
        self.fly_duration = 500
        self.fly_cooldown = 2000
        self.last_fly_time = -self.fly_cooldown

        # TODO Code electricity animation
        # imgaes can blit another on top
        # ex. self.image.blit(self.electricity_images[self.current_electricity_image])
        self.electricity_animation_cooldown = 100
        self.electricity_last_frame_changed = 0

    def move_left(self):
        self.rect.x -= self.player_speed

    def move_right(self):
        self.rect.x += self.player_speed

    def move_up(self):
        self.rect.y -= self.player_speed

    def move_down(self):
        self.rect.y += self.player_speed

    def handle_input(self, keys):

        if keys[pygame.K_d]:
            self.move_right()

        if keys[pygame.K_a]:
            self.move_left()

        if keys[pygame.K_w]:
            self.move_up()

        if keys[pygame.K_s]:
            self.move_down()


    def update(self, elapsed_time):
        pass

