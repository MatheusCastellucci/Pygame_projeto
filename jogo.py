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


all_enemies = pygame.sprite.Group()
for i in range(11):
    humberto = Enemy(humberto_img)
    all_enemies.add(humberto)

while game:
    clock.tick (FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    all_enemies.update()
    
    window.fill((0, 0, 0))
    window.blit(background, (10, 10))
    all_enemies.draw(window)
    
    pygame.display.update()


pygame.quit()
