# Drawing a Line
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 400))
screen.fill((200,200,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen, (0,0,0), [100,300], [500,300], 5)
    pygame.display.flip()