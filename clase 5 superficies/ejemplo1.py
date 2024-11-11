# Todo en pygame es una superficie
from recursos.paleta_colores import *
from recursos.configuraciones import *
import pygame

pygame.init()

# superficie vertical y horizontal
imagen_vertical = pygame.Surface((100, 100))
imagen_vertical.fill(VERDE)

# Repasar POO
rectangulo_vertical = imagen_vertical.get_rect() #obtengo rectangulo
rectangulo_vertical.center = (ANCHO // 2, ALTO // 2)

# HORIZONTAL
imagen_horizontal = pygame.Surface((100, 100))
imagen_horizontal.fill(BLANCO)

# Toda superficie se asocia a un rectángulo
rectangulo_horizontal = imagen_horizontal.get_rect() #obtengo rectangulo
rectangulo_horizontal.center = (ANCHO - (ANCHO // 4), ALTO // 2)

PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

clock = pygame.time.Clock()

bandera = True

while bandera:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
    
    PANTALLA.fill(NEGRO)
    
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)    
    
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)

    if rectangulo_vertical.colliderect(rectangulo_horizontal):        
        imagen_vertical.fill(BLANCO)
        imagen_horizontal.fill(VERDE)
    else:
        imagen_vertical.fill(VERDE)
        imagen_horizontal.fill(BLANCO)
    
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top == ALTO:
        rectangulo_vertical.y = 0    
    rectangulo_horizontal.x += 10
    if rectangulo_horizontal.left == ANCHO:
        rectangulo_horizontal.x = 0

    # crear dos ejes
    pygame.draw.line(PANTALLA, AZUL, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 3) #Y
    pygame.draw.line(PANTALLA, ROJO, (0, ALTO // 2), (ANCHO, ALTO // 2), 3) #X

    pygame.display.update()

pygame.quit()




