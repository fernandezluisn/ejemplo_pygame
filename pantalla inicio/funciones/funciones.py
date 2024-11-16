import pygame

def dibujar_boton(superficie: any, texto: str, color: tuple, texto_color: tuple,
                  x: int, y: int, ancho=200, alto=60):
    
    boton = pygame.Rect(x, y, ancho, alto)
    
    pygame.draw.rect(superficie, color, boton)
    fuente = pygame.font.SysFont("Arial", 13)
    superficie_texto = fuente.render(texto, True, texto_color)
    texto_color = superficie_texto.get_rect(center=boton.center)
    superficie.blit(superficie_texto, texto_color)

    return boton


def presionar_boton(boton: any, evento: any)->bool:
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if boton.collidepoint(evento.pos):
            return True
    return False