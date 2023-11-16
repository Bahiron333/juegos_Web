import pygame
import pygame.locals

class Ladrillo:

    def __init__(self,dificultad,lad_pregunta,posicion):

        self.imagen_ladrillo = pygame.image.load("img/ladrillo_facil.png").convert_alpha()
        self.ancho, self.alto = self.imagen_ladrillo.get_size()
        self.x, self.y = posicion
        #saber la dificultad del ladrillo
        if dificultad=="dificil":
           self.dificultad_lad=10
        elif dificultad=="medio":
           self.dificultad_lad=5
        elif dificultad=="facil":
           self.dificultad_lad=2
        self.ladrillo_pregunta = lad_pregunta
        self.ladrillo_sin_romper = True
        self.responder_pregunta = False
        self.tipo_ladrillo()
    
    #golpear la pelota lado de abajo
    def golpear_ladrillo(self,pelota):

        if(
            pelota.y<self.y+self.alto
            and pelota.y > self.y
            and pelota.x+pelota.ancho>self.x
            and pelota.x<self.x+self.ancho
        ):
            pelota.dir_y=-pelota.dir_y
            pelota.y=self.y+self.alto
            self.dificultad_lad -= 1



    def tipo_ladrillo(self):

        #ladrillo dificil
        if self.dificultad_lad == 10 or self.dificultad_lad == 9 or self.dificultad_lad == 8:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_dificil.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 7 or self.dificultad_lad == 6:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_dificil_roto.png").convert_alpha()
           self.ladrillo_sin_romper = True
        #ladrillo medio
        if self.dificultad_lad == 5 or self.dificultad_lad == 4:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_medio.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 3:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_medio_roto.png").convert_alpha()
           self.ladrillo_sin_romper = True
        #ladrillo facil
        if self.dificultad_lad == 2:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_facil.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 1:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_facil_roto.png").convert_alpha()
           self.ladrillo_sin_romper =True
        if self.dificultad_lad == 0 and self.ladrillo_pregunta == True:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_pregunta.png").convert_alpha()
           self.ladrillo_sin_romper = True
           self.responder_pregunta = True
        if self.dificultad_lad == 0 and self.ladrillo_pregunta != True:
           self.ladrillo_sin_romper=False#es verdadero cuando el ladrillo esta roto
           self.responder_pregunta = False
    


