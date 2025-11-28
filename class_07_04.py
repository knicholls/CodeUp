
# Activity
import sys
import pygame

resolution = ( 800,450)
screen = pygame.display.set_mode(resolution)
screen.fill((255,255,255))
pygame.display.flip
i = -1
colours = [(255,85,85),(255,125,65),(255,245,85),(85,205,85),(85,245,255),(65,55,130),(100,45,105)]


while True and i < len(colours):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN:
            i += 1
            screen.fill(colours[i])
            pygame.display.flip()