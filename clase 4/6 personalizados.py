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

# creo evento
evento_personalizado = pygame.USEREVENT

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.KEYDOWN:
            # están todas las teclas con k
            if evento.key == pygame.K_SPACE: #capturo un evento
                pygame.event.post(pygame.event.Event(evento_personalizado))
        elif evento.type == evento_personalizado:
            print("Se presionó espacio y se generó un evento personalizado")


        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
