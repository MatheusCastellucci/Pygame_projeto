import pygame
pygame.init()
from Consts import *
from assets import *

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    init_screen = pygame.image.load('imagens/init_screen.PNG').convert()
    init_screen = pygame.transform.scale(init_screen, (WIDTH, HEIGHT))
    init_screen_rect = init_screen.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((1, 1, 1))
        screen.blit(init_screen, init_screen_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def victory_screen(screen):
    clock = pygame.time.Clock()
    vict_screen = pygame.image.load('imagens/You Win.PNG').convert()
    vict_screen = pygame.transform.scale(vict_screen, (WIDTH, HEIGHT))
    vict_screen_rect = vict_screen.get_rect()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False
        screen.fill((1, 1, 1))
        screen.blit(vict_screen, vict_screen_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state

def defeat_screen(screen):
    clock = pygame.time.Clock()
    def_screen = pygame.image.load('imagens/Game Over.PNG').convert()
    def_screen = pygame.transform.scale(def_screen, (WIDTH, HEIGHT))
    def_screen_rect = def_screen.get_rect()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False
        screen.fill((1, 1, 1))
        screen.blit(def_screen, def_screen_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Professors Invasion!!')
assets = load_assets()

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

    def update(self):
        if self.rect.y >= 55 and assets['Verif_guzzo'] <= 9:
            self.speedx = 5
            self.speedy = 0
            assets['Verif_guzzo'] += 1
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

    def update(self):

        if self.rect.y >= 110 and assets['Verif_hum'] <= 9:
            self.speedx = 5
            self.speedy = 0
            assets['Verif_hum'] += 1

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
        

    def update(self):
        if self.rect.y >= 165 and assets['Verif_hage'] <= 9:
            self.speedx = 5
            self.speedy = 0
            assets['Verif_hage'] += 1

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

    def update(self):
        if self.rect.y >= 0 and assets['Verif_sergio'] <= 9:
            self.speedx = -5
            self.speedy = 0
            assets['Verif_sergio'] += 1
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

    def update(self):

        if self.rect.y >= -55 and assets['Verif_carlos'] <= 9:
            self.speedx = -5
            self.speedy = 0
            assets['Verif_carlos'] += 1

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
        

    def update(self):
        if self.rect.y >= -110 and assets['Verif_leo'] <= 9:
            self.speedx = -5
            self.speedy = 0
            assets['Verif_leo'] += 1

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


clock = pygame.time.Clock()
FPS = 60

all_sprites = pygame.sprite.Group()
all_guzzos = pygame.sprite.Group()
all_humbertos = pygame.sprite.Group()
all_hages = pygame.sprite.Group()
all_leonidas = pygame.sprite.Group()
all_sergio = pygame.sprite.Group()
all_carlos = pygame.sprite.Group()
all_insper = pygame.sprite.Group()
all_tirinhos = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_insper'] = all_insper
groups['all_guzzos'] = all_guzzos
groups['all_humberto'] = all_humbertos
groups['all_hages'] = all_hages
groups['all_carlos'] = all_carlos
groups['all_leonidas'] = all_leonidas
groups['all_sergio'] = all_sergio
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
    carlos = EnemyCarlos(assets)
    all_sprites.add(carlos)
    all_carlos.add(carlos)
    leo = EnemyLeo(assets)
    all_sprites.add(leo)
    all_leonidas.add(leo)
    sergio = EnemySergio(assets)
    all_sprites.add(sergio)
    all_sergio.add(sergio)

insper = EnemyINSPER(assets)
all_sprites.add(insper)
all_insper.add(insper)

def displayText(text):
    font = pygame.font.SysFont('', 50)
    message = font.render(text, False, (255, 255, 255))
    window.blit(message, (200, 160))

DONE = 0
PLAYING = 1
INIT = 2
VICTORY = 3
DEFEAT = 4

state = init_screen(window)

keys_down = {}
score = 0
vidas = 3
vidas_insper = 15
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
                if event.key == pygame.K_SPACE:
                    player.shoot()

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
        hits4 = pygame.sprite.groupcollide(all_sergio, all_tirinhos, True, True, pygame.sprite.collide_mask)
        hits5 = pygame.sprite.groupcollide(all_carlos, all_tirinhos, True, True, pygame.sprite.collide_mask)
        hits6 = pygame.sprite.groupcollide(all_leonidas, all_tirinhos, True, True, pygame.sprite.collide_mask)
        hits7 = pygame.sprite.groupcollide(all_insper, all_tirinhos, False, True, pygame.sprite.collide_mask)
        for hage in hits1: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1

        for humberto in hits2: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1

        for guzzo in hits3: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1
        
        for sergio in hits4: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1

        for carlos in hits5: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1

        for leo in hits6: 
            assets['mata_alien_prof'].play()
            score += 100
            if score % 5000 == 0 and vidas < 3:
                vidas += 1

        for insper in hits7:
            assets['mata_alien_prof'].play()
            vidas_insper -= 1
            if vidas_insper == 0:
                insper.kill()
                state = victory_screen(window)

        if humberto.rect.y > HEIGHT-20:
            vidas -= 1
            humberto.kill()
            if vidas == 0:
                state = DONE
        if hage.rect.y > HEIGHT-20:
            vidas -= 1
            hage.kill()
            if vidas == 0:
                state = DONE
        if guzzo.rect.y > HEIGHT-20:
            vidas -= 1
            guzzo.kill()
            if vidas == 0:
                state = DONE
        if sergio.rect.y > HEIGHT-20:
            vidas -= 1
            sergio.kill()
            if vidas == 0:
                state = DONE
        if carlos.rect.y > HEIGHT-20:
            vidas -= 1
            carlos.kill()
            if vidas == 0:
                state = DONE
        if leo.rect.y > HEIGHT-20:
            vidas -= 1
            leo.kill()
            if vidas == 0:
                state = DONE
        hits8 = pygame.sprite.spritecollide(player, all_hages, True, pygame.sprite.collide_mask)
        hits9 = pygame.sprite.spritecollide(player, all_humbertos, True, pygame.sprite.collide_mask)
        hits10 = pygame.sprite.spritecollide(player, all_guzzos, True, pygame.sprite.collide_mask)
        hits11 = pygame.sprite.spritecollide(player, all_sergio, True, pygame.sprite.collide_mask)
        hits12 = pygame.sprite.spritecollide(player, all_carlos, True, pygame.sprite.collide_mask)
        hits13 = pygame.sprite.spritecollide(player, all_leonidas, True, pygame.sprite.collide_mask)
        if len(hits8) > 0 or len(hits9) > 0 or len(hits10) > 0 or len(hits11) > 0 or len(hits12) > 0 or len(hits13) > 0:
            vidas -= 1
        if vidas == 0:
            state = defeat_screen(window)

        if len(all_humbertos) == 0 and len(all_guzzos) == 0 and len(all_hages) == 0:
            assets['Verif_guzzo'] = 0
            assets['Verif_hage'] = 0
            assets['Verif_hum'] = 0
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
        if len(all_carlos) == 0 and len(all_leonidas) == 0 and len(all_sergio) == 0:
            assets['Verif_sergio'] = 0
            assets['Verif_leo'] = 0
            assets['Verif_carlos'] = 0
            for x in range(1, 10):
                assets ['pos_x'] = 75
                assets ['pos_x'] *= x
                carlos = EnemyCarlos(assets)
                all_sprites.add(carlos)
                all_carlos.add(carlos)
                leo = EnemyLeo(assets)
                all_sprites.add(leo)
                all_leonidas.add(leo)
                sergio = EnemySergio(assets)
                all_sprites.add(sergio)
                all_sergio.add(sergio)
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