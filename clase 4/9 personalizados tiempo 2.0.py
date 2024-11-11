#clock controla velocidad del bucle
import pygame
import sys
import random

pygame.init()
width = 400
height = 400
pantalla = pygame.display.set_mode((width, height))

def definir_color()->tuple:
    color_r = random.randint(0, 255)
    color_g = random.randint(0, 255)
    color_b = random.randint(0, 255)

    return (color_r, color_g, color_b)   

AZUL_CLARO = (0, 100, 255)

pygame.display.set_caption("Eventos de tiempo")

bandera = True

clock = pygame.time.Clock()

# creo evento
CAMBIO_COLOR = pygame.USEREVENT + 5
pygame.time.set_timer(CAMBIO_COLOR, 2000)

color_fondo = (0, 0, 0)

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == CAMBIO_COLOR:            

            color_fondo = definir_color()          
            

    pantalla.fill(color_fondo)
    pygame.display.update()

        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
