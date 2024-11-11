#Rectangulos pueden ser objetos
#Cuando un método es privado, solo puede ser llamado desde otros métodos 
# dentro de la misma clase. Si intentas acceder a un método privado desde 
# fuera de la clase, Python lanzará un error.

import pygame

class Imagen2:

    def __init__(self, origen, tamaño, colores):
        # definir atributos como privados y devolver getters y setters
        self.__superficie = pygame.Surface(tamaño)
        self.__color = colores[0]
        self.__color_colision = colores[1]
        self.__superficie.fill(self.__color)#color por defecto

        self.__rectangulo = self.__superficie.get_rect() #obtengo rectangulo
        self.__rectangulo.center = (origen[0], origen[1])

    def mover(self, velocidad: int, sentido: str, 
                       pantalla: pygame.Surface):
        
        if sentido == "vertical":
            self.__rectangulo.y += velocidad
            if self.__rectangulo.top > pantalla.get_rect().height:
                self.__rectangulo.y = 0
        else:
            self.__rectangulo.x += velocidad
            if self.__rectangulo.left == pantalla.get_rect().width:
                self.__rectangulo.x = 0

    def get_superficie(self):
        return self.__superficie
    
    def get_rectangulo(self):
        return self.__rectangulo
    
    def detectar_colision(self, otra_imagen: "Imagen2"): 

        if self.__rectangulo.colliderect(otra_imagen.get_rectangulo()):
            self.__superficie.fill(self.__color_colision)
            #funciona porque son de la misma clase
            otra_imagen.__superficie.fill(otra_imagen.__color_colision)
        else:
            self.__superficie.fill(self.__color)
            otra_imagen.__superficie.fill(otra_imagen.__color)




    
        
