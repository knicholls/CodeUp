# Tic Tac Toe

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tic Tac Toe")

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
    pygame.draw.line(screen, white, (200 + 133 + 134, 200),(200 + 133 +134, 600))   
    pygame.draw.line(screen, white, (200, 200 + 133),(600, 200 + 133))   
    pygame.draw.line(screen, white, (200, 200 + 133 + 134),(600, 200 + 133 + 134))   

    clear_board_button = pygame.draw.rect(screen, (255,0,0),clear_button_rect)
    text_reset = font.render("Reset", True, (255,255,255))
    text_reset_rect = text_reset.get_rect()
    text_reset_rect.center = (400, 90)
    screen.blit(text_reset, text_reset_rect)

    pygame.display.update()

    class Board:
        def __init__(self):
            self.board_values = [["0","0","0"],
                                ["0","0","0"],
                                ["0","0","0"]]
