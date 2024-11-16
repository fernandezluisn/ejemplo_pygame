import pygame
from recursos.colores import *
from .funciones import *

def cambiar_ranking(superficie:any):
    superficie.fill(BLANCO)    

def jugar_juego(superficie:any):
    superficie.fill(VERDE)

def dar_inicio(pantalla:any)->tuple:
    btn_1 = dibujar_boton(pantalla, "Botón 1", AZUL, (215,215,215), 100, 100)
    btn_2 = dibujar_boton(pantalla, "Botón 2", AZUL, (215,215,215), 100, 300)

    return btn_1, btn_2

    