import pygame

# texto dinámico

lista_nombres = ["Pedro", "Jorge", "Juan", "Esteban", "Brian"]

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

ventana = pygame.display.set_mode((300,500))
pygame.display.set_caption("Mi juego")

ventana.fill(BLANCO)

icono = pygame.image.load("./pelota.jpg") 

# modulo.clase.metodo
pygame.display.set_icon(icono) 

fuente = pygame.font.SysFont("Arial", 13) # selecciono fuente


bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
          bandera = False

    altura = 100
    for nombre in lista_nombres: # explicar esto
       texto = fuente.render(nombre, False, NEGRO, ROJO)       
       ventana.blit(texto, (10,altura)) # Actualiza objetos del juego
       altura += 40
       
    
    pygame.display.update()

pygame.quit()

# cómo devolver ejecutable