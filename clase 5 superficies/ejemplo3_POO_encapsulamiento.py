# Cuando termina mostrar comparacion de codigo
from recursos.paleta_colores import *
from recursos.configuraciones import *
from recursos.Imagen2 import Imagen2
import pygame

# se utilizan clases

pygame.init()

# superficie vertical y horizontal publicas
imagen_vertical = Imagen2((ANCHO // 2, ALTO // 2), (100, 100), (VERDE, BLANCO))
imagen_horizontal = Imagen2((ANCHO - (ANCHO // 4), ALTO // 2), 
                           (100, 100), (BLANCO, VERDE))


PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

clock = pygame.time.Clock()

bandera = True

while bandera:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
    
    PANTALLA.fill(NEGRO)
    
    PANTALLA.blit(imagen_vertical.get_superficie(), 
                  imagen_vertical.get_rectangulo())    
    
    PANTALLA.blit(imagen_horizontal.get_superficie(), 
                  imagen_horizontal.get_rectangulo())

    
    imagen_horizontal.detectar_colision(imagen_vertical)
    
    imagen_horizontal.mover(10, "horizontal", PANTALLA)
    imagen_vertical.mover(10, "vertical", PANTALLA)

    # crear dos ejes
    pygame.draw.line(PANTALLA, AZUL, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 3) #Y
    pygame.draw.line(PANTALLA, ROJO, (0, ALTO // 2), (ANCHO, ALTO // 2), 3) #X

    pygame.display.update()

pygame.quit()