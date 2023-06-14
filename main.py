import pygame
import random
from spritesheet import Spritesheet
from explosion import Explosion
from stormhead import Stormhead
from player import Player


(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survivior')
FPS = 60
clock = pygame.time.Clock()






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





enemy_group = pygame.sprite.Group()


for i in range(100):
  baddie = Stormhead()
  randX = random.randint(500, width)
  randY = random.randint(0, height)
  baddie.rect.x = randX
  baddie.rect.y = randY
  enemy_group.add(baddie)

current_frame = 0
elapsed_time = 0


player = Player()

player_group = pygame.sprite.Group()
player_group.add(player)

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
  mouse = pygame.mouse.get_pressed()

  player.handle_input(keys, mouse, elapsed_time)

  # right mouse button pressed
  if player.can_galaxy_burst():
    explosion = Explosion(lv_images, player.rect.x + 200, player.rect.y)
    explosion_group.add(explosion)

  ##########################################
  #UPDATE###################################
  ##########################################

  player.update(elapsed_time)

  for baddie in enemy_group.sprites():
    baddie.update(elapsed_time)
    if baddie.rect.x > player.rect.x:
      baddie.rect.x -= baddie.speed
    else:
      baddie.rect.x += baddie.speed

    if baddie.rect.y < player.rect.y:
      baddie.rect.y += baddie.speed
    else:
      baddie.rect.y -= baddie.speed

  for explosion in explosion_group.sprites():
    explosion.update()
    if pygame.sprite.spritecollide(explosion, enemy_group, True):
      pass




  ##########################################
  #DRAW#####################################
  ##########################################

  screen.fill((64, 109, 107))

  player_group.draw(screen)
  player.draw(screen)

  enemy_group.draw(screen)
  explosion_group.draw(screen)


  pygame.display.flip()
  clock.tick(FPS)
