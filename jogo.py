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
NAVE_WIDTH = 50
NAVE_HEIGHT = 35
background = pygame.image.load('imagens/back.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
humberto_img = pygame.image.load('imagens/Ft_Humberto.png').convert_alpha()
humberto_img = pygame.transform.scale(humberto_img, (HUMBERTO_WIDTH, HUMBERTO_HEIGHT))
nave_img = pygame.image.load('imagens/nave.png').convert_alpha()
nave_img = pygame.transform.scale(nave_img, (NAVE_WIDTH, NAVE_HEIGHT))

class Ship(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
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

all_sprites = pygame.sprite.Group()
pos_x = 25
pos_y = 100
player = Ship(nave_img)
all_sprites.add(player)

for i in range(11):
    
    humberto = Enemy(humberto_img, pos_x, pos_y)
    all_sprites.add(humberto)
    pos_x += 70

while game:
    clock.tick (FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
                
    all_sprites.update()
    
    window.fill((0, 0, 0))
    window.blit(background, (10, 10))
    all_sprites.draw(window)
    
    pygame.display.update()


pygame.quit()