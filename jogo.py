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

width = 600
height = 600
PROFESSOR_WIDTH = 50
PROFESSOR_HEIGHT = 38
NAVE_WIDTH = 50
NAVE_HEIGHT = 35
TIRO_WIDTH = 1
TIRO_HEIGHT = 2

assets = {}
background = pygame.image.load('imagens/back.png')
assets ['background'] = pygame.transform.scale(background, (width, height))
humberto_img = pygame.image.load('imagens/Ft_Humberto.png')
assets ['humberto_img'] = pygame.transform.scale(humberto_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
hage_img = pygame.image.load('imagens/Hage.jpg')
assets ['hage_img'] = pygame.transform.scale(hage_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
guzzo_img = pygame.image.load('imagens/Guzzo.jpg')
assets ['guzzo_img'] = pygame.transform.scale(guzzo_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
nave_img = pygame.image.load('imagens/nave.png')
assets ['nave_img'] = pygame.transform.scale(nave_img, (NAVE_WIDTH, NAVE_HEIGHT))
tiro_img = pygame.image.load('imagens/tiro.png')
assets ['tiro_img'] = pygame.transform.scale(tiro_img, (TIRO_WIDTH, TIRO_HEIGHT))


pygame.mixer.music.load('sons/musiquinea.ogg')
pygame.mixer.music.set_volume(0.4)
assets['som_dano'] = pygame.mixer.Sound('sons/expl3.wav')
assets['mata_alien_prof'] = pygame.mixer.Sound('sons/expl6.wav')
assets['som_tirinho'] = pygame.mixer.Sound('sons/tirinho.wav')

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = nave_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 0
        self.groups = groups
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 200

    def upadate(self):
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        momento = pygame.time.get_ticks()
        elapsed_ticks = momento - self.last_shot

        if elapsed_ticks < self.shoot_ticks:
            self.shoot_ticks = momento
            novo_tiro = Bullet(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(novo_tiro )
            self.groups['all_bullets'].add(novo_tiro )
            self.assets['pew_sound'].play()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['meteor_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speedx = 0
        self.speedy = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1
            self.speedy = 0

class EnemyGUZZO:
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['guzzo_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speedx = 10
        self.speedy = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1

class EnemyHUM:
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y+50
        self.speedx = 10
        self.speedy = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1

class EnemyHUM:
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['hage_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y+100
        self.speedx = 10
        self.speedy = 0

    def upadate(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1
game = True

clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
pos_x = 55
pos_y = 50
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