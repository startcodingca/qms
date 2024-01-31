#Author: Norman
#Date Created: Jan 24, 2024
#QMS - Flappy Bird Game
#Lesson 1: left off printing event...next lesson close window function

import pygame

print(pygame.init())
                                                                    #(width, height)
screen = pygame.display.set_mode((500,700))

gameRunning = True
while gameRunning == True:
    for event in pygame.event.get():
        print(event)
