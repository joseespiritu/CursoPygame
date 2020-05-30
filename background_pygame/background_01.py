import pygame


""" EL MISMO TAMAÑO DE LA VENTANA DEBE SER EL MISMO QUE LA IMAGEN """
screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()

done = False

""" AÑADIENDO LA IMAGEN DE FONDO A LA PANTALLA """
background = pygame.image.load("01.png").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    """ VENTANA CON IMAGEN """
    screen.blit(background, [0,0])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()