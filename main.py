import pygame 
import pygame.locals
import game
import sys


def main():

    pygame.init()

    fondo = pygame.image.load("img/fondo.png")
    icono = pygame.image.load("img/icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Juego  Didactico")
    ventana = pygame.display.set_mode((1000,562))

    #texto de inicio de juego 
    font = pygame.font.SysFont('harrington',70,bold=True)
    letrero = font.render("Juego  Interactivo",False,('#A0522D'))


    #boton#######################33
    button_play = pygame.Rect(400,300,150,100)

    while True:

        ventana.blit(fondo,(0,0))
        ventana.blit(letrero,(185,140))

        #Agregar texto del boton
        font_boton = pygame.font.SysFont("harrington",50,bold=True)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    game.main_game()

        x, y = pygame.mouse.get_pos()

        if x >= button_play.x and x <= button_play.x+150 and y >= button_play.y and y <= button_play.y+100:
            pygame.draw.rect(ventana,("#CD853F"),button_play)
            text_boton = font_boton.render("Play",True,(255,255,255))

        else:
            pygame.draw.rect(ventana,("#8B4513"),button_play)
            text_boton = font_boton.render("Play",True,("#778899"))
        ventana.blit(text_boton,(button_play.x+23,button_play.y+20))

        pygame.display.update()

main()