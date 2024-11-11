import pygame

pygame.init()

pygame.display.set_mode((300,500))
pygame.display.set_caption("Mi juego")

bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()
    if(len(lista_eventos)>0):
        print(lista_eventos)
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False


pygame.quit()