# Tic Tac Toe

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font( 'freesansbold.ttf', 50)
small_font = pygame.font.Font( 'freesansbold.ttf', 20)
text_x = font.render("X", True, (255,255,255))
text_o = font.render("O", True, (255,255,255))

class Cordinate:
    def __init__(self, x,y):
        self.x = x
        self.y = y

clear_button_rect = pygame.Rect(300, 50, 200, 75)
mode_button_rect = pygame.Rect(575, 50, 175, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))

    white = ((255,255,255))
    pygame.draw.line(screen, white, (200 + 133, 200),(200 +133, 600))    
    pygame.draw.line(screen, white, (200 + 133, 200),(200 +133, 600))   
    pygame.draw.line(screen, white, (200 + 133, 200),(200 +133, 600))   
    pygame.draw.line(screen, white, (200 + 133, 200),(200 +133, 600))   
    
