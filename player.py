import pygame
from spritesheet import Spritesheet
from direction import Direction

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet('Char_3.png')

        # load images
        self.idle_image = ss.image_at((0, 0, 64, 64, ))
        self.idle_image.set_alpha()
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
        self.electricity_last_frame_changed = -self.electricity_animation_cooldown
        self.current_electricity_image = 0
        self.electricity_pos = [self.rect.x, self.rect.y]

        self.using_galaxy_burst = False
        self.current_frame = 0
        self.facing = Direction.RIGHT

    def move_left(self):
        self.rect.x -= self.player_speed
        self.electricity_pos[0] -= self.player_speed
        self.facing = Direction.LEFT

    def move_right(self):
        self.rect.x += self.player_speed
        self.electricity_pos[0] += self.player_speed
        self.facing = Direction.RIGHT

    def move_up(self):
        self.rect.y -= self.player_speed
        self.electricity_pos[1] -= self.player_speed

    def move_down(self):
        self.rect.y += self.player_speed
        self.electricity_pos[1] += self.player_speed

    def can_galaxy_burst(self):
        return self.using_galaxy_burst

    def handle_input(self, keys, mouse, elapsed_time):

        if self.in_flying_mode:
            self.player_speed = self.player_flying_speed
        else:
            self.player_speed = self.player_walk_speed

        if keys[pygame.K_d]:
            self.move_right()

        if keys[pygame.K_a]:
            self.move_left()

        if keys[pygame.K_w]:
            self.move_up()

        if keys[pygame.K_s]:
            self.move_down()

        if not self.in_flying_mode:
            if keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
                self.image = self.walking_image
            else:
                self.image = self.idle_image

        if keys[pygame.K_SPACE]:

            if elapsed_time - self.last_fly_time > self.fly_cooldown + self.fly_duration and not self.in_flying_mode:
                # WE CAN FLYYYY!!!!!!!!
                self.in_flying_mode = True
                self.image = self.flying_image
                self.last_fly_time = elapsed_time

        # left mouse button pressed
        if mouse[0]:
            pass

        if mouse[2]:
            self.using_galaxy_burst = True
        else:
            self.using_galaxy_burst = False

    def update(self, elapsed_time):

        if self.in_flying_mode:
            if elapsed_time - self.last_fly_time > self.fly_duration:
                self.in_flying_mode = False
                self.image = self.idle_image

        # self.image.blit(self.electricity_images[self.current_electricity_image], (self.rect.x, self.rect.y))

        if elapsed_time - self.electricity_last_frame_changed > self.electricity_animation_cooldown:
            self.current_frame += 1
            self.electricity_last_frame_changed = elapsed_time

    def draw(self, screen):
        if self.facing == Direction.RIGHT:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        screen.blit(self.electricity_images[self.current_frame % len(self.electricity_images)],
                    (self.electricity_pos[0], self.electricity_pos[1]))