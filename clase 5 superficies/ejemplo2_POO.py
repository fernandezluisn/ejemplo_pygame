# Todo en pygame es una superficie
from recursos.paleta_colores import *
from recursos.configuraciones import *
from recursos.Imagen import Imagen
import pygame

# se utilizan clases

pygame.init()

# superficie vertical y horizontal publicas
imagen_vertical = Imagen((ANCHO // 2, ALTO // 2), (100, 100), (VERDE, BLANCO))
imagen_horizontal = Imagen((ANCHO - (ANCHO // 4), ALTO // 2), 
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
    
    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)    
    
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)

    if imagen_vertical.rectangulo.colliderect(imagen_horizontal.rectangulo):        
        imagen_vertical.superficie.fill(imagen_vertical.color_colision)
        imagen_horizontal.superficie.fill(imagen_horizontal.color_colision)
    else:
        imagen_vertical.superficie.fill(imagen_vertical.color)
        imagen_horizontal.superficie.fill(imagen_horizontal.color)
    
    imagen_vertical.rectangulo.y += 10
    if imagen_vertical.rectangulo.top == ALTO:
        imagen_vertical.rectangulo.y = 0    
    imagen_horizontal.rectangulo.x += 10
    if imagen_horizontal.rectangulo.left == ANCHO:
        imagen_horizontal.rectangulo.x = 0

    # crear dos ejes
    pygame.draw.line(PANTALLA, AZUL, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 3) #Y
    pygame.draw.line(PANTALLA, ROJO, (0, ALTO // 2), (ANCHO, ALTO // 2), 3) #X

    pygame.display.update()

pygame.quit()