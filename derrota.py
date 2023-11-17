import pygame
import pygame.locals 
import sys

def main_derrota():
    
    pygame.init()

    icono = pygame.image.load("img/icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Juego  Didactico")
    windows_infor = pygame.display.set_mode((1000,562))

    main_image = pygame.image.load("img/derrota.png")
    windows_infor.blit(main_image,(0,0))

    font_letrero_continuar = pygame.font.SysFont('widelatin',40,bold=True)
    letrero_continuar = font_letrero_continuar.render("Inicio",True,(0,0,0))
  
    boton = pygame.Rect(350,400,250,100)

    informacion = True

    while informacion:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos): 
                    informacion=False
                    return False
            
        x,y = pygame.mouse.get_pos()#Odtenemos las coordenadas del mouse

        if boton.x <= x <= boton.x + 250 and boton.y <=y <= boton.y+100:
            pygame.draw.rect(windows_infor,("white"),boton,border_radius=30)
            letrero_continuar = font_letrero_continuar.render("inicio",True,("red"))
        else:
            pygame.draw.rect(windows_infor,("red"),boton,border_radius=30)
            letrero_continuar = font_letrero_continuar.render("inicio",True,("white"))

        windows_infor.blit(letrero_continuar,(375,428))
        pygame.display.update()



