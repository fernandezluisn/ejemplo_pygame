# Cuando termina mostrar comparacion de codigo
from recursos.paleta_colores import *
from recursos.configuraciones import *
from recursos.Imagen3 import Imagen3
import pygame

# se utilizan clases

pygame.init()

# superficie vertical y horizontal publicas
imagen_vertical = Imagen3((ANCHO // 2, ALTO // 2), (100, 100), 
                          "imagenes\pngwing.com.png")
imagen_horizontal = Imagen3((ANCHO - (ANCHO // 4), ALTO // 2), 
                           (100, 100), "imagenes\pngwing.com.png")


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

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
    
    PANTALLA.blit(fondo, (0, 0))    

    PANTALLA.blit(imagen_vertical.get_superficie(), 
                  imagen_vertical.get_rectangulo())    
    
    PANTALLA.blit(imagen_horizontal.get_superficie(), 
                  imagen_horizontal.get_rectangulo())    
    
    
    imagen_horizontal.mover(10, "horizontal", PANTALLA)
    imagen_vertical.mover(10, "vertical", PANTALLA)   

    pygame.display.update()

pygame.quit()