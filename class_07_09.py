#Detecting Collision ExaMPLE
import pygame


pygame.init
screen = pygame.display.set_mode((800,800))
rect_list = [(300,300,100,100), (600,600,50,70)]
pygame.draw.rect(screen, (255,0,0), rect_list[0])
pygame.draw.rect(screen, (0,0,255), rect_list[1])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse = pygame.Rect(pos[0], pos[1],1,1)
            idx = mouse.collidelist(rect_list)
            if idx != -1:
                pygame.draw.rect(screen, (255,255,255), rect_list[idx])
                pygame.display.flip()
