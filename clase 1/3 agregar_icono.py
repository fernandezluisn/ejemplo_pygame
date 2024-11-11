import pygame

# Quiero agregar icono

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

ventana = pygame.display.set_mode((300,500))
pygame.display.set_caption("Mi juego")

ventana.fill(ROJO)

icono = pygame.image.load("./pelota.jpg") #cargo imagen. A veces hay que usar r antes de la ruta o barras invertidas
pygame.display.set_icon(icono) #asigno el icono a la ventana

bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
          bandera = False

    pygame.display.update()

pygame.quit()

# cómo devolver ejecutable