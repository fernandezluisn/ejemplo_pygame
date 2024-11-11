#Rectangulos pueden ser objetos
import pygame

class Imagen:

    def __init__(self, origen, tamaño, colores):
        # definir atributos como privados y devolver getters y setters
        self.superficie = pygame.Surface(tamaño)
        self.color = colores[0]
        self.color_colision = colores[1]
        self.superficie.fill(self.color)#color por defecto

        self.rectangulo = self.superficie.get_rect() #obtengo rectangulo
        self.rectangulo.center = (origen[0], origen[1])

    