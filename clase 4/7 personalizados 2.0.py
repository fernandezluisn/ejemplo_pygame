#clock controla velocidad del bucle
import pygame
import sys

pygame.init()
width = 400
height = 400
pantalla = pygame.display.set_mode((width, height))

AZUL_CLARO = (0, 100, 255)

pygame.display.set_caption("Eventos de teclado")

bandera = True

clock = pygame.time.Clock()

tiempo_inicial = pygame.time.get_ticks()

print(tiempo_inicial)

# creo evento
evento_personalizado = pygame.USEREVENT

EVENTO_MOVERSE_ARRIBA = pygame.USEREVENT

EVENTO_MOVERSE_ABAJO = pygame.USEREVENT + 1

EVENTO_MOVERSE_DERECHA = pygame.USEREVENT + 2

EVENTO_MOVERSE_IZQUIERDA = pygame.USEREVENT + 3


print(EVENTO_MOVERSE_ARRIBA)
print(EVENTO_MOVERSE_ABAJO) # Puedo calcular eventos con números

x = 100
y = 200

while bandera:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.KEYDOWN:
            # están todas las teclas con k
            if evento.key == pygame.K_w: #capturo un evento
                pygame.event.post(pygame.event.Event(EVENTO_MOVERSE_ARRIBA))
            elif evento.key == pygame.K_s: #capturo un evento
                pygame.event.post(pygame.event.Event(EVENTO_MOVERSE_ABAJO))
            elif evento.key == pygame.K_d: #capturo un evento
                pygame.event.post(pygame.event.Event(EVENTO_MOVERSE_DERECHA))
            elif evento.key == pygame.K_a: #capturo un evento
                pygame.event.post(pygame.event.Event(EVENTO_MOVERSE_IZQUIERDA))
        elif evento.type == EVENTO_MOVERSE_ARRIBA:
            y -= 10
        elif evento.type == EVENTO_MOVERSE_ABAJO:
            y += 10
        elif evento.type == EVENTO_MOVERSE_IZQUIERDA:
            x -= 10
        elif evento.type == EVENTO_MOVERSE_DERECHA:
            x += 10

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, AZUL_CLARO, (x, y, 200, 100), 4)#x,y,ancho y alto   
    pygame.display.update()

        
    
        
    clock.tick(15)  # Baja las ejecuciones por segundo del while, default = 60  

pygame.quit()
sys.exit()
