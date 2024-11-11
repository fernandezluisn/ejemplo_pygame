#clock controla velocidad del bucle
import pygame
import sys

width = 400
height = 400

x = 30
y = 100
altura_rectangulo = 50
ancho_rectangulo = 50
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
        elif evento.type == pygame.KEYDOWN:
            # están todas las teclas con k
            if evento.key == pygame.K_LEFT: #capturo un evento
                x -= velocidad
            elif evento.key == pygame.K_RIGHT: #capturo un evento
                x += velocidad
            elif evento.key == pygame.K_DOWN: 
                y += velocidad
            elif evento.key == pygame.K_UP: #capturo un evento
                y -= velocidad    

            # cambiar color con un click      
        elif evento.type == pygame.MOUSEBUTTONDOWN: 

            mouse_x = evento.pos[0]
            mouse_y = evento.pos[1]

            if (mouse_x >= x and 
                mouse_x <= (x + ancho_rectangulo)) and (mouse_y >= y 
                and mouse_y <= (y + altura_rectangulo)):
                if color_rectangulo == ROJO:
                    color_rectangulo = BLANCO
                else:
                    color_rectangulo = ROJO         
            

    pantalla.fill((0, 0, 0))

    pygame.draw.rect(pantalla, color_rectangulo, 
                     (x, y, ancho_rectangulo, altura_rectangulo), 7)

    pygame.display.update()

        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
