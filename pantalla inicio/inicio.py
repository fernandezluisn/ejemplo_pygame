import pygame
from funciones.funciones import dibujar_boton, presionar_boton
from funciones.pantallas import *
from recursos.colores import *

pygame.init()

pantalla = pygame.display.set_mode((700,700))
pygame.display.set_caption("Mi juego")

modalidad = 1

bandera = True

while bandera == True:

    if modalidad == 1: 
        btn_1, btn_2 = dar_inicio(pantalla)        
    elif modalidad == 2:
        cambiar_ranking(pantalla)
    elif modalidad == 3:
        jugar_juego(pantalla)


    
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        elif presionar_boton(btn_1, evento) and modalidad == 1:
            modalidad = 2            
            print("Se apretó botón 1")
        elif presionar_boton(btn_2, evento) and modalidad == 1:
            modalidad = 3
            print("Se apretó botón 2")
    
    pygame.display.update()
    



pygame.quit()