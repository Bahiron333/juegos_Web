import pygame 
import pygame.locals
import sys
from raqueta import *
from pelota import *
from ladrillo import *

def main_game():

    pygame.init()

    icono = pygame.image.load("img/icono.ico")
    fondo_list = pygame.image.load("img/fondo_juego.png")

    pygame.display.set_caption("Juegos Didacticos")
    pygame.display.set_icon(icono)
    win_list = pygame.display.set_mode((1000,562))

    paleta = raqueta()

    paleta.y = 500
    pelota = PelotaP("img/pelota.png")

    #ladrillos list
    ladrillo = Ladrillo("dificil",True,(500,500))
    
    while True:

        win_list.blit(fondo_list,(0,0))
        win_list.blit(paleta.imagen,(paleta.x,paleta.y))
        win_list.blit(pelota.imagen,(pelota.x,pelota.y))
        paleta.movimiento()
        paleta.golpear(pelota)

        pelota.movimiento()
        pelota.rebotar()

        if ladrillo.ladrillo_sin_romper:
            win_list.blit(ladrillo.imagen_ladrillo,(500,500))
            ladrillo.tipo_ladrillo()
            ladrillo.golpear_ladrillo(pelota)
            if ladrillo.responder_prgunta:
                main_pregunta()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paleta.dir_x = -8
                if event.key == pygame.K_RIGHT:
                    paleta.dir_x = 8
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    paleta.dir_x=0
                if event.key==pygame.K_RIGHT:
                    paleta.dir_x=0



        pygame.display.update()
                
def main_pregunta():
    pass