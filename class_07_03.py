# Decting Mouse Input
import pygame

pygame.init
w = 640
h = 480
screen = pygame.display.set_mode((w,h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #Left Click
                print("Left Click")
            if event.button == 2: 
                #Middle Click
                print("Middle Click")
            if event.button == 3: 
                #Right Click
                print("Right Click")
              
