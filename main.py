import pygame

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Titulo e Icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
player_speed = 0.5


def player(x, y):
    screen.blit(playerImg, (x, y))


# Loop do jogo
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((200, 200, 255))

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

    playerX += playerX_change
    player(playerX, playerY)

    pygame.display.update()
