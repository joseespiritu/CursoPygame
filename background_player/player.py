import pygame

""" EL MISMO TAMAÑO DE LA VENTANA DEBE SER EL MISMO QUE LA IMAGEN """
screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()

done = False

""" AÑADIENDO LA IMAGEN DE FONDO A LA PANTALLA """
background = pygame.image.load("background.png").convert()
player = pygame.image.load("nave01.png").convert()
pygame.mouse.set_visible(0)

#Quitando fondo de la imagen
player.set_colorkey([0,0,0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #OBTENER COORDENADAS DEL MOUSE
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]

    """ VENTANA CON IMAGEN """
    screen.blit(background, [0,0])
    screen.blit(player, [x,y])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()