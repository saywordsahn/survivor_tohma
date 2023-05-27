import pygame
from spritesheet import Spritesheet
from explosion import Explosion
from stormhead import Stormhead
from player import Player


(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survivior')
FPS = 60
clock = pygame.time.Clock()




ss= Spritesheet('Char_3.png')

image = ss.image_at((0, 0, 64, 64, ))
flying_image = ss.image_at((64 * 2, 64 * 1, 64, 64 ))
walking_image = ss.image_at((64,64,64,64))

electricity = ss.load_strip((64*0, 64*6, 64, 64), 4, (0, 0, 0))
electricity_pos = [100 - 64, 100]

# coin_ss = spritesheet.spritesheet('coins.png')
# coin_images = coin_ss.load_strip((0, 0, 16, 16), 6, (0, 0, 0))


# load effects
lv_sheet = Spritesheet('effects/fx2_electric_burst_large_violet/spritesheet.png')
lv_images = lv_sheet.load_strip((0, 0, 72, 72), 16, (0, 0, 0))

# create an explosion

explosion_group = pygame.sprite.Group()


# # stormhead
# stormhead_run_images = Spritesheet('stormhead/run.png').load_strip_vert((0, 0, 119, 124), 10, -1)
# stormhead = Stormhead(stormhead_run_images)

baddie = Stormhead()

enemy_group = pygame.sprite.Group()
enemy_group.add(baddie)


animation_cooldown = 100
last_frame_changed = 0
current_frame = 0
elapsed_time = 0

player_sprite = pygame.sprite.Sprite()
player_sprite.image = image
player_sprite.rect = player_sprite.image.get_rect()
player_sprite.rect.topright = (100, 100)
player_walk_speed = 3
player_flying_speed = 8
player_speed = 2
in_flying_mode = False
in_walking_mode = False
fly_duration = 500
fly_cooldown = 2000
last_fly_time = -fly_cooldown

player_group = pygame.sprite.Group()
player_group.add(player_sprite)


# new player
# TODO: replace older player and player_group with Player class
new_player = Player()

new_player_group = pygame.sprite.Group()
new_player_group.add(new_player)

running = True

while running:

  time = clock.get_time()
  elapsed_time += time


  ###########################################
  #INPUT#####################################
  ###########################################
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


  keys = pygame.key.get_pressed()

  new_player.handle_input(keys)

  if in_flying_mode:
    player_speed = player_flying_speed
  else:
    player_speed = player_walk_speed

  if keys[pygame.K_d]:
    player_sprite.rect.x += player_speed
    electricity_pos[0]  += player_speed

  #  if not in_walking_mode:
  #    in_walking_mode = True
  if keys[pygame.K_w]:
    player_sprite.rect.y -= player_speed
    electricity_pos[1] -= player_speed
  if keys[pygame.K_a]:
    player_sprite.rect.x -= player_speed
    electricity_pos[0] -= player_speed
  if keys[pygame.K_s]:
    player_sprite.rect.y += player_speed
    electricity_pos[1] += player_speed
  if not in_flying_mode:
    if keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
      player_sprite.image = walking_image
    else:
      player_sprite.image = image

  if keys[pygame.K_SPACE]:

    if elapsed_time - last_fly_time > fly_cooldown + fly_duration and not in_flying_mode:
      # WE CAN FLYYYY!!!!!!!!
      in_flying_mode = True
      player_sprite.image = flying_image
      last_fly_time = elapsed_time

  mouse = pygame.mouse.get_pressed()

  # left mouse button pressed
  if mouse[0]:
    pass

  # right mouse button pressed
  if mouse[2]:
    explosion = Explosion(lv_images, player_sprite.rect.x + 200, player_sprite.rect.y)
    explosion_group.add(explosion)



  ##########################################
  #UPDATE###################################
  ##########################################

  for explosion in explosion_group.sprites():
    explosion.update()

  if elapsed_time - last_frame_changed > animation_cooldown:
    current_frame += 1
    last_frame_changed = elapsed_time

  if in_flying_mode:
    if elapsed_time - last_fly_time > fly_duration:

      in_flying_mode = False
      player_sprite.image = image


  ##########################################
  #DRAW#####################################
  ##########################################

  screen.fill(0)

  player_group.draw(screen)
  new_player_group.draw(screen)
  screen.blit(electricity[current_frame % len(electricity)], (electricity_pos[0], electricity_pos[1]))

  enemy_group.draw(screen)
  explosion_group.draw(screen)



  pygame.display.flip()
  clock.tick(FPS)

