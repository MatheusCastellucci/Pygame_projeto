import pygame
from sklearn.preprocessing import scale
from Consts import *

def assets_organizer(elemento):
    print('imagens/' + elemento[0] + '.' + elemento[1])
    load_image = pygame.image.load('imagens/' + elemento[0] + '.' + elemento[1]).convert()
    scale_image = pygame.transform.scale(load_image, (informacoes_get(elemento[2]+'_WIDTH'), informacoes_get(elemento[2]+'_HEIGHT')))
    return scale_image

def load_assets():
    assets = {}

    for elemento in elementos:
        assets[elemento[0].lower()+'_img'] = assets_organizer(elemento)
        if elemento[2] == 'PROFESSOR':
            assets['Verif_'+elemento[0].lower()]=0

    tiro_img = pygame.image.load('imagens/tiro.png').convert_alpha()
    assets['tiro_img'] = pygame.transform.scale(tiro_img, (TIRO_WIDTH, TIRO_HEIGHT))
    assets['pos_y'] = 50


    assets["fonte_score"] = pygame.font.Font('fontes/PressStart2P.ttf', 28)
    assets['pew_sound'] = pygame.mixer.Sound('sons/tirinho.wav')
    pygame.mixer.music.load('sons/musiquinea.wav')
    pygame.mixer.music.set_volume(0.2)
    assets['som_dano'] = pygame.mixer.Sound('sons/expl3.wav')
    assets['mata_alien_prof'] = pygame.mixer.Sound('sons/expl6.wav')
    assets['som_tirinho'] = pygame.mixer.Sound('sons/tirinho.wav')
    return assets