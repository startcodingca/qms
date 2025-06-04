import pygame, os

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
pygame.init()
file_path = os.path.dirname(__file__)
spaceship_image = pygame.image.load(os.path.join(file_path, 'spaceship.png'))

clock = pygame.time.Clock()

#==== CONSTANTS=====
W = 400
H = 600

YELLOW = (255,255,0)
RED = (255,0,0)

#====SET UP=====
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("QMS - Spring 2025 - GALAGA")

p1size = 50
p1x = 175
p1y = 520

laser_size = 20
laser_x = p1x
laser_y = p1y
laser_shooting = False

gameRun = True
while gameRun == True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameRun = False

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        p1x = p1x + 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        p1x = p1x - 5

    if p1x < 0:
        p1x = 5
    if p1x > 400-p1size:
        p1x = 395-p1size

    screen.fill((0,0,0))
    pygame.draw.rect(screen, YELLOW, (p1x, p1y, p1size, p1size))

    #when we press on SPACE BAR (to shoot.)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if laser_shooting == False:
            laser_x = p1x
            laser_y = p1y
            laser_shooting = True
    if laser_shooting == True:
        laser_y = laser_y - 10
        if laser_y < 0:
            laser_shooting = False
        pygame.draw.rect(screen, RED, (laser_x, laser_y, laser_size, laser_size))
    pygame.display.update()
    clock.tick(100)

pygame.quit()
