# Drawing a Rectangle
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

    pygame.draw.rect(screen, (0,0,255), [100,100,400,100], 2)
    pygame.display.flip()