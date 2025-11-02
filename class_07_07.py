# Displaying Text
import pygame

def main():
    pygame.init()
    display_surface = pygame.display.set_mode((640, 480))
    font = pygame.font.Font( 'freesansbold.ttf', 64)

    text = font.render("I love PyGame!", True, (255,238,140), (63,60,35))
    textRect = text.get_rect()

    textRect.center = (320,240)
    display_surface.blit(text, textRect)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit

if __name__ == '__main__':
    main()