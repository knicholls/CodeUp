# Collisions Activity
import pygame
pygame.init()

# screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Remove Rectangles")

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create list of white rects
rects = []
for i in range(5):
    rect = pygame.Rect(50 + i * 100, 150, 50, 50)
    rects.append(rect)

running = True
while running:
    screen.fill(BLACK)

    # draw white rects
    for r in rects:
        pygame.draw.rect(screen, WHITE, r)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#solution starts here
        # when you click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # for each rectangle
            for r in rects:
                # if the rectangle collides with the mouse (when the mouse is clicked)
                if r.collidepoint(mouse_pos):
                    # remove rectangle
                    rects.remove(r)
#solution ends here

pygame.quit()