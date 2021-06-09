import pygame
from Consts import *
from assets import *

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['nave_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 350

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        momento = pygame.time.get_ticks()
        elapsed_ticks = momento - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = momento
            novotiro = Tirinho(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_tirinhos'].add(novotiro)
            self.groups['all_sprites'].add(novotiro)
            self.assets['pew_sound'].play()

class EnemyGUZZO(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['guzzo_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] - 165
        self.speedx = 0
        self.speedy = 3
        self.assets = assets

    def update(self):
        if self.rect.y >= 55 and self.assets['Verif_guzzo'] <= 9:
            self.speedx = 5
            self.speedy = 0
            self.assets['Verif_guzzo'] += 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1

class EnemyHUM(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] - 110
        self.speedx = 0
        self.speedy = 3
        self.assets = assets

    def update(self):

        if self.rect.y >= 110 and self.assets['Verif_hum'] <= 9:
            self.speedx = 5
            self.speedy = 0
            self.assets['Verif_hum'] += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1

class EnemyHAGE(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['hage_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] -55
        self.speedx = 0
        self.speedy = 3
        self.assets = assets
        

    def update(self):
        if self.rect.y >= 165 and self.assets['Verif_hage'] <= 9:
            self.speedx = 5
            self.speedy = 0
            self.assets['Verif_hage'] += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1
        if self.rect.y >= HEIGHT-20:
            self.kill()

class EnemySergio(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['sergio_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] - 220
        self.speedx = 0
        self.speedy = 3
        self.assets = assets

    def update(self):
        if self.rect.y >= 0 and self.assets['Verif_sergio'] <= 9:
            self.speedx = -5
            self.speedy = 0
            self.assets['Verif_sergio'] += 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1

class EnemyCarlos(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['carlos_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] - 275
        self.speedx = 0
        self.speedy = 3
        self.assets = assets

    def update(self):

        if self.rect.y >= -55 and self.assets['Verif_carlos'] <= 9:
            self.speedx = -5
            self.speedy = 0
            self.assets['Verif_carlos'] += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1

class EnemyLeo(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['leo_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y'] - 330
        self.speedx = 0
        self.speedy = 3
        self.assets = assets
        

    def update(self):
        if self.rect.y >= -110 and self.assets['Verif_leo'] <= 9:
            self.speedx = -5
            self.speedy = 0
            self.assets['Verif_leo'] += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y += 50
            self.speedx *= -1
        if self.rect.y >= HEIGHT-20:
            self.kill()

class EnemyINSPER(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['insper_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = assets['pos_x']
        self.rect.y = assets['pos_y']
        self.speedx = 2.75
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.speedx *= -1

class Tirinho(pygame.sprite.Sprite):
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