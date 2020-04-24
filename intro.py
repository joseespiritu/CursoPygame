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

#CONTROLAR LOS FPS
clock = pygame.time.Clock()

# COORDENADAS DEL CUADRADO
cord_x = 400
cord_y = 200

# VELOCIDAD A LA QUE SE MOVERA EL CUADRADO
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # LOGICA        
    if (cord_x > 720 or cord_x < 0):
        speed_x  *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1
    
    cord_x += speed_x
    cord_y += speed_y
    
    
    # COLOR DE FONDO
    screen.fill(WHITE)
    
    # ZONA DE DIBUJO
    """ pygame.draw.line(screen, GREEN, [0,100], [100,100], 5)
    pygame.draw.rect(screen, BLACK, (100,100,80,80))
    pygame.draw.circle(screen, BLACK, (200,200), 30) """
    
    """ for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
        pygame.draw.line(screen, GREEN, (x, 0), (x,100), 5) """
    
    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
    
    # ACTUALIZAR PANTALLA
    pygame.display.flip()
    clock.tick(60)