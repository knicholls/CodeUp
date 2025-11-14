# Display a string in a Pygame Window
import sys
import pygame

pygame.font.init()
x = 600
y = 350


display_surface = pygame.display.set_mode((x, y))
font = pygame.font.Font('freesansbold.ttf', 32)
string = input("Enter a sentence: ")
text = font.render(string[0:20], True, (0,255,0), (0,0,128))
textRect = text.get_rect()
textRect.center = (300,175)
display_surface.blit(text, textRect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()