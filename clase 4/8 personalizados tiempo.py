#clock controla velocidad del bucle
import pygame
import sys

pygame.init()
width = 400
height = 400
pantalla = pygame.display.set_mode((width, height))

AZUL_CLARO = (0, 100, 255)

pygame.display.set_caption("Eventos de tiempo")

bandera = True

clock = pygame.time.Clock()

# Se desplaza texto cada segundo
mensaje = "Hola"

x, y = 100, 100
fuente = pygame.font.SysFont("arial", 30)

# creo evento
pygame.time.set_timer(pygame.USEREVENT, 1000)

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.USEREVENT:
            x += 10
            

    pantalla.fill((0, 0, 0))
    texto = fuente.render(mensaje, True, (255, 255, 255))
    pantalla.blit(texto, (x, y))
    pygame.display.update()

        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
