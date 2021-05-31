import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Professors Invasion!!')

PROFESSOR_WIDTH = 60
PROFESSOR_HEIGHT = 48
NAVE_WIDTH = 1
NAVE_HEIGHT = 1
TIRO_WIDTH = 1
TIRO_HEIGHT = 2

assets = {}
background = pygame.image.load('imagens/back.png').convert()
assets['background'] = pygame.transform.scale(background, (WIDTH, HEIGHT))

humberto_img = pygame.image.load('imagens/Ft_Humberto.png').convert()
assets['humberto_img'] = pygame.transform.scale(humberto_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

hage_img = pygame.image.load('imagens/Hage.jpg').convert()
assets['hage_img'] = pygame.transform.scale(hage_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

guzzo_img = pygame.image.load('imagens/Guzzo.jpg').convert()
assets['guzzo_img'] = pygame.transform.scale(guzzo_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

nave_img = pygame.image.load('imagens/nave.png').convert_alpha()
assets['nave_img'] = pygame.transform.scale(nave_img, (NAVE_WIDTH, NAVE_HEIGHT))

tiro_img = pygame.image.load('imagens/tiro.png').convert()
assets['tiro_img'] = pygame.transform.scale(tiro_img, (TIRO_WIDTH, TIRO_HEIGHT))
assets['pos_y'] = 50

assets["fonte_score"] = pygame.font.Font('fontes/PressStart2P.ttf', 28)

pygame.mixer.music.load('sons/musiquinea.ogg')
pygame.mixer.music.set_volume(0.05)
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

    def update(self):
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
            novo_tiro = TIRINHO(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(novo_tiro )
            self.groups['all_bullets'].add(novo_tiro )
            self.assets['pew_sound'].play()

class EnemyGUZZO(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['guzzo_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y']
        self.speedx = 3
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1

class EnemyHUM(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] + 55
        self.speedx = 3
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1

class EnemyHAGE(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['hage_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] + 110
        self.speedx = 3
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 38
            self.speedx *= -1

class TIRINHO(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['tiro_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

game = True

clock = pygame.time.Clock()
FPS = 60

all_sprites = pygame.sprite.Group()
all_guzzos = pygame.sprite.Group()
all_humbertos = pygame.sprite.Group()
all_hages = pygame.sprite.Group()
all_tirinhos = pygame.sprite.Group()
groups = {}
groups['all_guzzos'] = all_guzzos
groups['all_humberto'] = all_humbertos
groups['all_hages'] = all_hages
groups['all_tirinhos'] = all_tirinhos 

player = Ship(groups, assets)
all_sprites.add(player)

for x in range(1, 10):
    assets ['pos_x'] = 75
    assets ['pos_x'] *= x
    humberto = EnemyHUM(assets)
    all_sprites.add(humberto)
    all_humbertos.add(humberto)
    hage = EnemyHAGE(assets)
    all_sprites.add(hage)
    all_hages.add(hage)
    guzzo = EnemyGUZZO(assets)
    all_sprites.add(guzzo)
    all_guzzos.add(guzzo)

def displayText(text):
    font = pygame.font.SysFont('', 50)
    message = font.render(text, False, (255, 255, 255))
    window.blit(message, (200, 160))

DONE = 0
PLAYING = 1

state = PLAYING

keys_down = {}
score = 0
vidas = 3

pygame.mixer.music.play(loops=-1)

while state != DONE:
    clock.tick (FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
    
        if state == PLAYING:
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

    if state == PLAYING:
        hits1 = pygame.sprite.groupcollide(all_hages, all_tirinhos, True, True, pygame.sprite.collide_mask)
        hits2 = pygame.sprite.groupcollide(all_humbertos, all_tirinhos, True, True, pygame.sprite.collide_mask)
        hits3 = pygame.sprite.groupcollide(all_guzzos, all_tirinhos, True, True, pygame.sprite.collide_mask)
        for hage in hits1: 
            assets['mata_alien_prof'].play()

            score += 100
            if score % 1000 == 0 and vidas <= 3:
                vidas += 1

        for humberto in hits2: 
            assets['mata_alien_prof'].play()

            score += 100
            if score % 1000 == 0 and vidas <= 3:
                vidas += 1

        for guzzo in hits3: 
            assets['mata_alien_prof'].play()

            score += 100
            if score % 1000 == 0 and vidas <= 3:
                vidas += 1
        
        if humberto.rect.y > HEIGHT-20:
            vidas -= 1
            if vidas == 0:
                state = DONE


    window.fill((0, 0, 0))
    window.blit(assets['background'], (0, 0))

    all_sprites.draw(window)

    text_surface = assets['fonte_score'].render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    text_surface = assets['fonte_score'].render(chr(9829) * vidas, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    window.blit(text_surface, text_rect)
    
    pygame.display.update()


pygame.quit()