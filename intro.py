import pygame, sys
pygame.init()

size = (800,500)

# CREAR VENTANA
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
