import pygame

# Quiero pintar la pantalla

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

ventana = pygame.display.set_mode((300,500)) #guardamos variable
pygame.display.set_caption("Mi juego")

ventana.fill(ROJO) #Asigno color

bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
          bandera = False

    pygame.display.update() #actualizo pantalla

pygame.quit()