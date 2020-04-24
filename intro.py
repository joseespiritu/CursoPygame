import pygame, sys
pygame.init()

# DEFINIR COLORES
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size = (800,500)

# CREAR VENTANA
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    # COLOR DE FONDO
    screen.fill(WHITE)
    
    # ZONA DE DIBUJO
    """ pygame.draw.line(screen, GREEN, [0,100], [100,100], 5)
    pygame.draw.rect(screen, BLACK, (100,100,80,80))
    pygame.draw.circle(screen, BLACK, (200,200), 30) """
    
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
        pygame.draw.line(screen, GREEN, (x, 0), (x,100), 5)
    
    # ACTUALIZAR PANTALLA
    pygame.display.flip()
