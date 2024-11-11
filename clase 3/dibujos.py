# Cómo trabajar posicionamiento en pantalla
# Cómo trabajar funciones

import pygame


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.display.set_caption("Prueba imágenes")

icono = pygame.image.load("clase 1\pelota.jpg") 
pygame.display.set_icon(icono) 

ventana_ppal.fill(BLANCO)

# Dibujo triangulo
# pygame.draw.line(ventana_ppal, AZUL, (30,30), (30, 500), 4) #linea vertical (x, y)
# pygame.draw.line(ventana_ppal, ROJO, (30,500), (730, 500), 6) #linea horizontal (x, y)
# pygame.draw.line(ventana_ppal, VERDE, (30,30), (730, 500), 3) #linea diagonal (x, y)

# jugar con las lineas

# pygame.draw.rect(ventana_ppal, VERDE, (90, 600, 100, 150),5)#x,y,ancho y alto
# pygame.draw.rect(ventana_ppal, AZUL_CLARO, (90, 600, 200, 100), 4)#x,y,ancho y alto

# circulos
# pygame.draw.circle(ventana_ppal,NEGRO,(700, 700),100)#recibe punto central y radio

#elipse: punto de origen, largo, ancho
pygame.draw.ellipse(ventana_ppal, AZUL_CLARO, (590, 180, 200, 100), 4)#x,y,ancho y alto

# Poligonos
puntos = [(100, 300), (100, 100), (250, 100)]
pygame.draw.polygon(ventana_ppal, VERDE, puntos,8)

# Ver estrella

bandera = True

while bandera:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            bandera = False


    pygame.display.update()

pygame.quit()