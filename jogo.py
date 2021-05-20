import pygame

White = (255, 255, 255)
Red = (255, 0, 0)
Black= (0, 0, 0)
Green = (0, 255, 0)
Gold = (255, 215, 0)
Blue = (0, 0, 250)


pygame.init()

WIDTH = 800
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Professors Invasion!!')

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYUP:
            game = False

    window.fill((0, 0, 0))

    pygame.display.update()


pygame.quit()