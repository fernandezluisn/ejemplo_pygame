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
        elif evento.type == pygame.KEYDOWN:#Se ejecuta cuando presiono
            print(f"Tecla presionada: {evento.key}")#muestro valos ascii de tecla presionada

pygame.quit()
sys.exit()