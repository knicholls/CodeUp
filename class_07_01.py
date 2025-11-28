#Detecting Mouse Button
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
            print("You just clicked!")

   
