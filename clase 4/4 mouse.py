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
        elif evento.type == pygame.MOUSEMOTION:#movimiento del mouse
            #Puedo usar coordenadas
            #x, y = evento.pos  
            x = evento.pos[0]      
            y = evento.pos[1]      
            print(f"{x}, {y}")
        elif evento.type == pygame.MOUSEWHEEL: #Ruedita del mouse
            print(evento.y)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                print("Click izquierdo")
            elif evento.button == 2:
                print("Click ruedita")
            elif evento.button == 3:
                print("Click derecho")
            else:
                print(evento.button)

        

pygame.quit()
sys.exit()