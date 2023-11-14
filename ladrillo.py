import pygame
import pygame.locals

class Ladrillo:

    def __init__(self,dificultad,lad_pregunta,posicion):

        self.imagen_ladrillo = pygame.image.load("img/ladrillo_facil.png").convert_alpha()
        self.ancho, self.alto = self.imagen_ladrillo.get_size()
        self.x, self.y = posicion
        self.dificultad_lad = dificultad
        self.ladrillo_pregunta = lad_pregunta
        self.ladrillo_sin_romper = True
        self.tipo_ladrillo()

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
            print(self.dificultad_lad)


    def tipo_ladrillo(self):

        if self.dificultad_lad == 4 or self.dificultad_lad == 3:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_dificil.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 2:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_medio.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 1:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_facil.png").convert_alpha()
           self.ladrillo_sin_romper =True
        if self.dificultad_lad == 0 and self.ladrillo_pregunta == True:
           self.imagen_ladrillo = pygame.image.load("img/ladrillo_pregunta.png").convert_alpha()
           self.ladrillo_sin_romper = True
        if self.dificultad_lad == 0 and self.ladrillo_pregunta != True:
            self.ladrillo_sin_romper=False#es verdadero cuando el ladrillo esta roto
    


