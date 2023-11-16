import pygame

p1y = 250

pygame.init( )

screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption('QMS 2023 - Pong')

gameRunning = True
while gameRunning == True:
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameRunning = False
        if pygame.key.get_pressed()[pygame.K_s]:
            p1y = p1y + 5
        if pygame.key.get_pressed()[pygame.K_w]:
            p1y = p1y - 5

    screen.fill( (214,214,214) )
                            #1.where? #2 colour? #3(xcoor, ycoor, width, height)
    pygame.draw.rect(screen, (169,46,213), (20, p1y,  25, 100) )
    pygame.display.update()

pygame.quit()



    
