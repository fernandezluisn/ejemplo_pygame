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

pygame.display.set_caption("Universo")
fondo = pygame.image.load(r"imagenes\universo.jpg")#expresion regular
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

pygame.mixer.music.load("sonidos\space-odyssey.mp3")
pygame.mixer.music.play()# reproduce una sola vez o en bucle con -1
pygame.mixer.music.set_volume(0.5)

clock = pygame.time.Clock()

bandera = True

while bandera:
    clock.tick(FPS)
    PANTALLA.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
    
    
    
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