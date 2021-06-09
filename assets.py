import pygame
from Consts import *

def load_assets():
    assets = {}
    background = pygame.image.load('imagens/back.png').convert()
    assets['background'] = pygame.transform.scale(background, (WIDTH, HEIGHT))

    humberto_img = pygame.image.load('imagens/Ft_Humberto.png').convert_alpha()
    assets['humberto_img'] = pygame.transform.scale(humberto_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    hage_img = pygame.image.load('imagens/Hage.jpg').convert()
    assets['hage_img'] = pygame.transform.scale(hage_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    guzzo_img = pygame.image.load('imagens/Guzzo.jpg').convert()
    assets['guzzo_img'] = pygame.transform.scale(guzzo_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    Sergio_img = pygame.image.load('imagens/Sergio.jpg').convert_alpha()
    assets['sergio_img'] = pygame.transform.scale(Sergio_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    Carlos_img = pygame.image.load('imagens/Carlos.jpg').convert()
    assets['carlos_img'] = pygame.transform.scale(Carlos_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    Leo_img = pygame.image.load('imagens/Leonidas.jpg').convert()
    assets['leo_img'] = pygame.transform.scale(Leo_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))

    insper_img = pygame.image.load('imagens/Inspu.png').convert_alpha()
    assets['insper_img'] = pygame.transform.scale(insper_img, (INSPER_WIDTH, INSPER_HEIGHT))

    nave_img = pygame.image.load('imagens/nave.png').convert_alpha()
    assets['nave_img'] = pygame.transform.scale(nave_img, (NAVE_WIDTH, NAVE_HEIGHT)) 

    tiro_img = pygame.image.load('imagens/tiro.png').convert_alpha()
    assets['tiro_img'] = pygame.transform.scale(tiro_img, (TIRO_WIDTH, TIRO_HEIGHT))
    assets['pos_y'] = 50

    assets['Verif_guzzo'] = 0
    assets['Verif_hage'] = 0
    assets['Verif_hum'] = 0
    assets['Verif_sergio'] = 0
    assets['Verif_leo'] = 0
    assets['Verif_carlos'] = 0

    assets["fonte_score"] = pygame.font.Font('fontes/PressStart2P.ttf', 28)
    assets['pew_sound'] = pygame.mixer.Sound('sons/tirinho.wav')
    pygame.mixer.music.load('sons/musiquinea.wav')
    pygame.mixer.music.set_volume(0.2)
    assets['som_dano'] = pygame.mixer.Sound('sons/expl3.wav')
    assets['mata_alien_prof'] = pygame.mixer.Sound('sons/expl6.wav')
    assets['som_tirinho'] = pygame.mixer.Sound('sons/tirinho.wav')
    return assets