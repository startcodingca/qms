import pygame, random

pygame.init( )
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

bird_y = 300
yspeed = 0
canJump = True

pipe_x = 800
pipe_y = random.randint(350, 550)

gamerunning = True
while gamerunning == True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gamerunning = False

    if pygame.key.get_pressed()[pygame.K_SPACE] and canJump == True:
      yspeed = -25
      canJump = False

    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
      canJump = True

  bird_y = bird_y + yspeed
  yspeed += 1.65

  if pipe_x < -100:
    pipe_x = 900
    pipe_y = random.randint(350,550)

  pipe_x -= 8
  
  screen.fill((204, 230, 255))
  pygame.draw.rect(screen, (0,0,0), (300, bird_y, 40, 40))
  pygame.draw.rect(screen, (0,255,0), (pipe_x, pipe_y, 100, 600))
  pygame.display.update()
  clock.tick(25)

pygame.quit()

