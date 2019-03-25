import pygame, sys, glob, os
from pygame import *

h = 800
w = 1400

screen = pygame.display.set_mode((w, h))
bg = pygame.image.load("game/bg.png")
table = pygame.image.load("game/table.png")
cook = pygame.image.load("game/Ramsay.png")
klient1 = pygame.image.load("game/client_down.png")
klient2 = pygame.image.load("game/client_up.png")
klient3 = pygame.image.load("game/client_right.png")
klient4 = pygame.image.load("game/client_left.png")


clock = pygame.time.Clock()


while 1:
    screen.fill((238, 238, 238))
    clock.tick(60)
    screen.blit(bg, (0, 0))

    screen.blit(table, (400, 100))
    screen.blit(table, (400, 400))
    screen.blit(table, (900, 100))
    screen.blit(table, (900, 400))

    screen.blit(cook, (50, 50))

    screen.blit(klient1, (980, 170))
    screen.blit(klient2, (565, 575))
    screen.blit(klient3, (920, 515))
    screen.blit(klient4, (630, 220))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()