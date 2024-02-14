#Author: Norman
#Date Created: Jan 24, 2024
#QMS - Flappy Bird Game

import pygame

print(pygame.init())
clock = pygame.time.Clock()
                                                                    #(width, height)
screen = pygame.display.set_mode((500,700))

birdy = 300

gameRunning = True
while gameRunning == True:
    for event in pygame.event.get():
        print(event)

    birdy = birdy + 10

    screen.fill((204, 255, 255)) #sky blue
    pygame.draw.rect(screen, (123,234,0), (250,birdy,50,50))
    pygame.display.update()#render
    clock.tick(50)
