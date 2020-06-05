import pygame
import random

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Imagem de fundo
background = pygame.image.load('background.png')

# Titulo e Icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 64*8
playerX_change = 0
player_speed = 8

# Inimigo
inimigoImg = pygame.image.load('alien.png')
inimigoX = random.randint(0, 800)
inimigoY = 0
inimigo_speed = 6
inimigoX_change = inimigo_speed
inimigoY_change = 64


def player(x, y):
    screen.blit(playerImg, (x, y))


def inimigo(x, y):
    screen.blit(inimigoImg, (x, y))


# Loop do jogo
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((200, 200, 230))
    # Imagem de fundo
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Se uma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # Atualiza posicao do player
    playerX += playerX_change

    # Garante que o player nao ultrapasse o limite da tela
    if playerX < 0:
        playerX = 0
    if playerX > 800 - 64:
        playerX = 800 - 64

    # Atualiza posicao do inimigo
    inimigoX += inimigoX_change

    # Garante que o player nao ultrapasse o limite da tela
    if inimigoX < 0:
        inimigoX = 0
        inimigoX_change = -inimigoX_change
        inimigoY += inimigoY_change
    if inimigoX > 800 - 64:
        inimigoX = 800 - 64
        inimigoX_change = -inimigoX_change
        inimigoY += inimigoY_change

    player(playerX, playerY)
    inimigo(inimigoX, inimigoY)

    pygame.display.update()
