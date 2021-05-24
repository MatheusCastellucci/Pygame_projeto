import pygame
import random
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

HUMBERTO_WIDTH = 50
HUMBERTO_HEIGHT = 38
background = pygame.image.load('imagens/back.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
humberto_img = pygame.image.load('imagens/Ft_Humberto.png').convert_alpha()
humberto_img = pygame.transform.scale(humberto_img, (HUMBERTO_WIDTH, HUMBERTO_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-HUMBERTO_HEIGHT)
        self.rect.y = 100
        self.speedx = 0
        self.speedy = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-HUMBERTO_WIDTH)
            self.rect.y = 100
            self.speedx = 0
            self.speedy = 0


game = True

clock = pygame.time.Clock()
FPS = 30

humberto1 = Enemy(humberto_img)
humberto2 = Enemy(humberto_img)
humberto3 = Enemy(humberto_img)
humberto4 = Enemy(humberto_img)
humberto5 = Enemy(humberto_img)
humberto6 = Enemy(humberto_img)
humberto7 = Enemy(humberto_img)
humberto8 = Enemy(humberto_img)
humberto9 = Enemy(humberto_img)
humberto10 = Enemy(humberto_img)
humberto11 = Enemy(humberto_img)

while game:
    clock.tick (FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    humberto1.update()
    humberto2.update()
    humberto3.update()
    humberto4.update()
    humberto5.update()
    humberto6.update()
    humberto7.update()
    humberto8.update()
    humberto9.update()
    humberto10.update()
    humberto11.update()
    
    window.fill((0, 0, 0))
    window.blit(background, (10, 10))
    window.blit(humberto1.image, humberto1.rect)
    window.blit(humberto2.image, humberto2.rect)
    window.blit(humberto3.image, humberto3.rect)
    window.blit(humberto4.image, humberto4.rect)
    window.blit(humberto5.image, humberto5.rect)
    window.blit(humberto6.image, humberto6.rect)
    window.blit(humberto7.image, humberto7.rect)
    window.blit(humberto8.image, humberto8.rect)
    window.blit(humberto9.image, humberto9.rect)
    window.blit(humberto10.image, humberto10.rect)
    window.blit(humberto11.image, humberto11.rect)
    pygame.display.update()


pygame.quit()
