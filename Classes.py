import pygame
from sympy import false, true
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

def Create_Enemy(self, assets, prof, pos_y):
    self.image = assets[prof + '_img']
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.rect.x = assets['pos_x']
    self.rect.y = assets['pos_y'] - pos_y
    self.speedx = 0
    self.speedy = 3
    self.assets = assets

def Update_Enemy(self, pos_y, prof, boolean, speedx):
    if self.rect.y >= pos_y and self.assets['Verif_' + prof] <= 9:
        self.speedx = speedx
        self.speedy = 0
        self.assets['Verif_' + prof] += 1

    self.rect.x += self.speedx
    self.rect.y += self.speedy
    
    if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
        self.rect.y += 50
        self.speedx *= -1

    if self.rect.y >= HEIGHT-20 and boolean:
        self.kill()

class EnemyGUZZO(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'guzzo', 165)

    def update(self):
        Update_Enemy(self, 55, 'guzzo', false, 5)

class EnemyHUM(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'humberto', 110)

    def update(self):
        Update_Enemy(self, 110, 'humberto', false, 5)

class EnemyHAGE(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'hage', 55)

    def update(self):
        Update_Enemy(self, 165, 'hage', true, 5)

class EnemySergio(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'sergio', 220)

    def update(self):
        Update_Enemy(self, 0, 'sergio', false, -5)

class EnemyCarlos(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'carlos', 275)

    def update(self):
        Update_Enemy(self, -55, 'carlos', false, -5)

class EnemyLeo(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        Create_Enemy(self, assets, 'leonidas', 330)

    def update(self):
        Update_Enemy(self, -110, 'leonidas', true, -5)

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