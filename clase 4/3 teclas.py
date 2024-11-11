import pygame
import sys

#Existe un modulo que me permite saber el valor de una tecla

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
            nombre = pygame.key.name(evento.key)# transforma el ascii a nombre
            print(f"Tecla presionada: {nombre}")
        
        

pygame.quit()
sys.exit()