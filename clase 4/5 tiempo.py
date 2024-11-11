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

tiempo_inicial = pygame.time.get_ticks()

print(tiempo_inicial)

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    if (tiempo_transcurrido % 100) == 0:
        print(tiempo_transcurrido * 0.001) 
    else:
        print(f"{(tiempo_transcurrido * 0.001):.02f}")   
        
    clock.tick(1)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
