import pygame
from pygame.locals import *
import sys

ventanaHor=1000#Ventana horizontal
ventanaVer=562#ventana vertical

class raqueta:
    def __init__(self):
        pygame.init()
        try:
            self.imagen=pygame.image.load("img/raqueta.png").convert_alpha()#imagen
        except:
            sys.exit()
        self.ancho,self.alto = self.imagen.get_size()
        self.x=ventanaHor/2-self.ancho
        self.y=0
        self.dir_x=0#direccion igual a 0


    def movimiento(self):
        self.x+=self.dir_x
        if self.x<=0:
           self.x = 0
        if self.x+self.ancho>=ventanaHor:
            self.x=ventanaHor-self.ancho

    def golpear(self,pelota):
        if(
            pelota.y+self.alto > self.y
            and pelota.y < self.y + self.alto 
            and pelota.x+pelota.ancho>self.x
            and pelota.x<self.x+self.ancho
        ):
            pelota.dir_y=-pelota.dir_y
            pelota.y=self.y-self.alto

    def reinicio(self):
        self.x=ventanaHor/2-self.ancho/2

