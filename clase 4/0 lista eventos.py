# Qué es un evento? es cuando sucede algo y el programa debe dar respuesta
# debo controlar los eventos

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
        #print(evento)# interacción con usuario y teclado        
        if evento.type == pygame.QUIT:
            bandera = False

pygame.quit()
sys.exit()#asegura que el programa finalizó