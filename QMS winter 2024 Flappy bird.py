import pygame, random, time

pygame.init( )
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

bird_x = 300
bird_y = 300
yspeed = 0
canJump = True
birdscore = 0

pipe_x = 800
pipe_y = random.randint(350, 550)

scorefontstyle = pygame.font.Font('freesansbold.ttf', 50)
scoretext = scorefontstyle.render("Score: " + str(birdscore), True, (0,0,0), None)

gameoverfontstyle = pygame.font.Font('freesansbold.ttf', 150)
gameovertext = gameoverfontstyle.render("GAME OVER", True, (255,0,0), (0,0,0))

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
    birdscore = birdscore + 1
    scoretext = scorefontstyle.render("Score: " + str(birdscore), True, (0,0,0), None)
    pipe_x = 900
    pipe_y = random.randint(350,550)

  pipe_x -= 8

  #====COLLISIONS====

  if bird_y > 600:
    screen.blit(gameovertext, (0, 200))
    pygame.display.update()
    gamerunning = False
    time.sleep(2)

  if bird_x + 40 > pipe_x and bird_x < pipe_x + 100 and bird_y > pipe_y:
    gamerunning = False
    time.sleep(2)

  if bird_x + 40 > pipe_x and bird_x < pipe_x + 100 and bird_y < pipe_y  - 250:
    gamerunning = False
    time.sleep(2)
  
  screen.fill((204, 230, 255))
  pygame.draw.rect(screen, (0,0,0), (bird_x, bird_y, 40, 40))
  pygame.draw.rect(screen, (0,255,0), (pipe_x, pipe_y, 100, 600))
  pygame.draw.rect(screen, (0,255,0), (pipe_x, pipe_y - 250 - 600, 100, 600))
  screen.blit(scoretext, (300,0))
  pygame.display.update()
  clock.tick(25)

pygame.quit()

