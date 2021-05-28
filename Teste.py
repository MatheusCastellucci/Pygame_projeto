#TESTE PROVISORIO DO JOGO(VAI MUDAR VIU)

import pygame

pygame.init()

width = 600
height = 600
PROFESSOR_WIDTH = 50
PROFESSOR_HEIGHT = 38
NAVE_WIDTH = 50
NAVE_HEIGHT = 35
background = pygame.image.load('imagens/back.png')
background = pygame.transform.scale(background, (width, height))
humberto_img = pygame.image.load('imagens/Ft_Humberto.png')
humberto_img = pygame.transform.scale(humberto_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
hage_img = pygame.image.load('imagens/nave.png')
hage_img = pygame.transform.scale(hage_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
guzzo_img = pygame.image.load('imagens/nave.png')
guzzo_img = pygame.transform.scale(guzzo_img, (PROFESSOR_WIDTH, PROFESSOR_HEIGHT))
nave_img = pygame.image.load('imagens/nave.png')
nave_img = pygame.transform.scale(nave_img, (NAVE_WIDTH, NAVE_HEIGHT))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Professors Invasion!!")
isPlaying = True

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        playerImg = nave_img
        screen.blit(playerImg, (self.x, self.y))

class EnemyHUM:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 200

    def draw(self):
        enemyImg = humberto_img 
        screen.blit(enemyImg, (self.x, self.y))
        self.y += 0.81

    def detectCollision(self):
        for laser in lasers:
            if (laser.x > self.x and
                    laser.x < self.x + 50 and
                    laser.y > self.y and
                    laser.y < self.y + 50):
                lasers.remove(laser)
                enemies.remove(self)

class EnemyGUZZO:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 200

    def draw(self):
        enemyImg2 = guzzo_img 
        screen.blit(enemyImg2, (self.x, self.y))
        self.y += 0.81

    def detectCollision(self):
        for laser in lasers:
            if (laser.x > self.x and
                    laser.x < self.x + 50 and
                    laser.y > self.y and
                    laser.y < self.y + 50):
                lasers.remove(laser)
                enemies.remove(self)

class EnemyHAGE:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 200

    def draw(self):
        enemyImg3 = hage_img
        screen.blit(enemyImg3, (self.x, self.y))
        self.y += 0.81

    def detectCollision(self):
        for laser in lasers:
            if (laser.x > self.x and
                    laser.x < self.x + 50 and
                    laser.y > self.y and
                    laser.y < self.y + 50):
                lasers.remove(laser)
                enemies.remove(self)
class Laser:
    def __init__(self, x, y):
        self.x = x + 25
        self.y = y - 10  

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(self.x, self.y, 2, 5))
        self.y -= 3


# Create Player object
player = Player((width/2)-25, height - 50)

# Enemies list
enemies = []

#lasers list
lasers = []

# Spawn enemies
for x in range(1, 10):
    enemies.append(EnemyHUM(x * 55, 50))
    enemies.append(EnemyHAGE(x * 55, 100))
    enemies.append(EnemyGUZZO(x * 55, 150))

def displayText(text):
    font = pygame.font.SysFont('', 50)
    message = font.render(text, False, (255, 255, 255))
    screen.blit(message, (200, 160))

clock = pygame.time.Clock()
while isPlaying:
    clock.tick (60)
    screen.blit(background, (0, 0))
    player.draw()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if player.x > 20:
            player.x -= 2
    elif pressed[pygame.K_RIGHT]:
        if player.x < width - 40:
            player.x += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            lasers.append(Laser(player.x, player.y))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            lasers.append(Laser(player.x, player.y))

    for enemy in enemies:
        enemy.draw()
        enemy.detectCollision()
        if enemy.y > height-32:
            displayText("PERDESTE")

    for laser in lasers:
        laser.draw()

    i = 0
    if len(enemies) <= 0:
        lasers = []
        for x in range(1, 10):
            enemies.append(EnemyHUM(x * 55, 50))
            enemies.append(EnemyHAGE(x * 55, 100))
            enemies.append(EnemyGUZZO(x * 55, 150))
        enemy.draw()
        enemy.detectCollision()
        if enemy.y > height-20:
            displayText("PERDESTE")

    pygame.display.update()