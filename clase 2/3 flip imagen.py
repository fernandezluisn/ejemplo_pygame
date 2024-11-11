import pygame

# Escalar imagenes en la ventana

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.display.set_caption("Prueba imágenes")

icono = pygame.image.load("clase 1\pelota.jpg") #cargo imagen. A veces hay que usar r antes de la ruta o barras invertidas
pygame.display.set_icon(icono) #asigno el icono a la ventana

imagen = pygame.image.load("clase 2\\inter.png") # ver tamaño
otra_imagen = pygame.image.load("clase 2\\milan.png") # ver tamaño

otra_imagen = pygame.transform.scale(otra_imagen, (250,250)) #explicar
otra_imagen = pygame.transform.flip(otra_imagen, True, False) #explicar

bandera = True

while bandera:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            bandera = False
    ventana_ppal.blit(imagen, (60, 60))
    ventana_ppal.blit(otra_imagen, (300, 60))

    pygame.display.update()

pygame.quit()