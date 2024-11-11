#clock controla velocidad del bucle
import pygame
import sys

width = 400
height = 400

x = 30
y = 100
velocidad = 5
direccion = 1

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

color_rectangulo = BLANCO



pygame.init()
pantalla = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Eventos de tiempo")
clock = pygame.time.Clock()

# creo evento
pygame.time.set_timer(pygame.USEREVENT, 100)

bandera = True

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.USEREVENT:        
            
            if x == (width-50) or x ==0:                
                direccion *= -1                 
            

            x += direccion * velocidad
                     
            

    pantalla.fill((0, 0, 0))

    pygame.draw.rect(pantalla, color_rectangulo, (x, y, 50, 50), 7)

    pygame.display.update()

        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
