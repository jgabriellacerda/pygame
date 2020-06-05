import pygame

#Inicializa o pygame
pygame.init()

#Cria a tela
screen = pygame.display.set_mode((800,600))

#Titulo e Icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


#Loop do jogo
running = True
while running:

    #RGB - Red, Green, Blue
    screen.fill((200, 200, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()

