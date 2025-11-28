# Filling The Screen
import sys
import pygame

resolution = (800,450)
color = (235,0,0)
screen = pygame.display.set_mode(resolution)

while True:
    screen.fill(color)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit