import pygame
import sys

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Eventos de teclado")

bandera = True

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.KEYDOWN:
            print(f"Tecla presionada: {evento.key}")
        elif evento.type == pygame.KEYUP:# captura el evento de soltar una tecla
            print("Se soltó la tecla")

pygame.quit()
sys.exit()