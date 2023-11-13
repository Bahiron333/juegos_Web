import pygame 
import pygame.locals


def main_list():

    pygame.init()
    
    icono = pygame.image.loand("img/icono.ico")
    fondo = pygame.image.load("img/fondo.png")

    pygame.display.set_caption("Juegos Didacticos")
    pygame.display.set_icon(icono)
    win_list = pygame.display.set_mode((1000,562))

    while True:

        win_list.blit(fondo,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                