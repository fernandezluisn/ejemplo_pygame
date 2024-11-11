#clock controla velocidad del bucle
import pygame
import sys

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Eventos de teclado")

bandera = True

clock = pygame.time.Clock()

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while  

pygame.quit()
sys.exit()
