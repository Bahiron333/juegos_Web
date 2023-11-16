import pygame
import pygame.locals 
import sys

def main_victoria():
    
    pygame.init()

    icono = pygame.image.load("img/icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Pong")
    windows_infor = pygame.display.set_mode((1000,562))


    font_texto= pygame.font.SysFont('arial',60,bold=False)
    main_image = pygame.image.load("img/victoria.png")
    letrero_texto = font_texto.render("!Has Ganado¡",True,(0,0,0))
    windows_infor.blit(main_image,(0,0))
    windows_infor.blit(letrero_texto,(280,350))

    font_letrero_continuar = pygame.font.SysFont('arial',40,bold=True)
    letrero_continuar = font_letrero_continuar.render("Inicio",True,(0,0,0))
  
    boton = pygame.Rect(280,480,230,60)
    windows_infor.blit(letrero_continuar,(370,488))

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

        if boton.x <= x <= boton.x + 230 and boton.y <=y <= boton.y+60:
            pygame.draw.rect(windows_infor,("#FFA500"),boton)
            letrero_continuar = font_letrero_continuar.render("inicio",True,(255,255,255))
        else:
            pygame.draw.rect(windows_infor,("#FFD700"),boton)
            letrero_continuar = font_letrero_continuar.render("inicio",True,(0,0,0))

        windows_infor.blit(letrero_continuar,(370,488))
        pygame.display.update()


