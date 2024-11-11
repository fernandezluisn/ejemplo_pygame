import pygame

# Rotar imagenes
# Trabaja con grados

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

icono = pygame.image.load("../clase 1\pelota.jpg") 
pygame.display.set_icon(icono) 

imagen = pygame.image.load("milan.png") 

# flip recibe 3 parametros
# Ahorra recursos. Con una imagen hago todo
# imagen = pygame.transform.flip(imagen,False, False) #No hace nada
imagen = pygame.transform.rotate(imagen,29) 


bandera = True

while bandera:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            bandera = False
    ventana_ppal.blit(imagen, (60, 60))    


    pygame.display.update()

pygame.quit()