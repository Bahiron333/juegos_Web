import pygame 
import pygame.locals
import sys
from raqueta import *
from pelota import *
from ladrillo import *
from derrota import *
from victoria import *
from main_pregunta import *

def main_game():

    pygame.init()

    icono = pygame.image.load("img/icono.ico")
    fondo_list = pygame.image.load("img/fondo_juego.png")

    pygame.display.set_caption("Juego Didactico")
    pygame.display.set_icon(icono)
    win_list = pygame.display.set_mode((1000,562))

    #fuente mostrar vida dentro de raqueta
    font_vidas = pygame.font.SysFont('arial',20,bold=False)

    paleta = raqueta()

    paleta.y = 500
    pelota = PelotaP("img/pelota.png")

    #ladrillos list
    ladrillos = [ 

        #Primera fila
        Ladrillo("facil",False,(5,20)), 
        Ladrillo("medio",True,(131,20)), 
        Ladrillo("dificil",False,(258,20)), 
        Ladrillo("dificil",False,(378,20)), 
        Ladrillo("medio",False,(509,20)), 
        Ladrillo("dificil",True,(635,20)), 
        Ladrillo("dificil",False,(761,20)),
        Ladrillo("facil",True,(887,20)),

        #segunda fila
        Ladrillo("medio",False,(5,71)), 
        Ladrillo("dificil",False,(131,71)), 
        Ladrillo("dificil",True,(258,71)), 
        Ladrillo("medio",False,(378,71)), 
        Ladrillo("dificil",True,(509,71)), 
        Ladrillo("facil",False,(635,71)), 
        Ladrillo("medio",False,(761,71)),
        Ladrillo("dificil",False,(887,71)),

        #tercera fila
        Ladrillo("dificil",False,(5,121)), 
        Ladrillo("facil",False,(131,121)), 
        Ladrillo("medio",True,(258,121)), 
        Ladrillo("facil",False,(378,121)), 
        Ladrillo("medio",True,(509,121)), 
        Ladrillo("dificil",False,(635,121)), 
        Ladrillo("dificil",False,(761,121)),
        Ladrillo("medio",True,(887,121)),

        #cuarta fila
        Ladrillo("medio",True,(5,171)), 
        Ladrillo("dificil",False,(131,171)), 
        Ladrillo("facil",False,(258,171)), 
        Ladrillo("dificil",False,(378,171)), 
        Ladrillo("dificil",False,(509,171)), 
        Ladrillo("medio",False,(635,171)), 
        Ladrillo("facil",True,(761,171)),
        Ladrillo("dificil",False,(887,171)),

        #quinta fila
        Ladrillo("dificil",True,(5,221)), 
        Ladrillo("facil",False,(131,221)), 
        Ladrillo("medio",True,(258,221)), 
        Ladrillo("facil",False,(378,221)), 
        Ladrillo("medio",True,(509,221)), 
        Ladrillo("facil",False,(635,221)), 
        Ladrillo("dificil",False,(761,221)),
        Ladrillo("medio",False,(887,221)),

        #sexta fila
        Ladrillo("facil",False,(5,271)), 
        Ladrillo("medio",True,(131,271)), 
        Ladrillo("facil",False,(258,271)), 
        Ladrillo("medio",False,(378,271)), 
        Ladrillo("facil",False,(509,271)), 
        Ladrillo("facil",True,(635,271)), 
        Ladrillo("medio",False,(761,271)),
        Ladrillo("facil",False,(887,271)),
    ]
        
    
    #variable para selecionar el numero de la pregunta 
    num_pregunta = 15


    while True:

        text_vidas = font_vidas.render(str(pelota.vidas),True,(0,0,0))

        win_list.blit(fondo_list,(0,0))
        win_list.blit(paleta.imagen,(paleta.x,paleta.y))
        win_list.blit(text_vidas,(paleta.x+80,paleta.y+12))
        win_list.blit(pelota.imagen,(pelota.x,pelota.y))
        paleta.movimiento()
        paleta.golpear(pelota)

        pelota.movimiento()
        pelota.rebotar(paleta)

        num_pregunta = function_ladrillos(ladrillos,win_list,pelota,num_pregunta)

        if pelota.vidas <= 0:
            main_derrota()
            break
        if victoria(ladrillos):
            main_victoria()
            break


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


        #pygame.time.Clock().tick(70)
        pygame.display.update()

#funcion que comprueba si todos los ladrillos estan roto
def victoria(ladrillos):

    ganador = False
    for ladrillo in ladrillos:
        if ladrillo.ladrillo_sin_romper:#si el ladrillo no esta roto no hay victoria
            ganador = False
            break
        else:
            ganador = True
    return ganador 


def function_ladrillos(ladrillos,ventana,pelota,numero_pregunta):

    pregunta = Pregunta(ventana)

    for ladrillo in ladrillos:
        if ladrillo.ladrillo_sin_romper:
            ventana.blit(ladrillo.imagen_ladrillo,(ladrillo.x,ladrillo.y))
            ladrillo.tipo_ladrillo()
            ladrillo.golpear_ladrillo(pelota)
            if ladrillo.responder_pregunta == True and ladrillo.dificultad_lad == -1:
               pregunta.escoger_pregunta(numero_pregunta,pelota)
               ladrillo.ladrillo_sin_romper=False
               numero_pregunta -= 1
    return numero_pregunta
                
     
    
    