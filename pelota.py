import pygame
from pygame.locals import *
import random
import sys

ventanaHor=1000#Ventana horizontal
ventanaVer=562#ventana vertical

class PelotaP:
    def __init__(self,fichero_imagen):
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()#imagen pelota
        self.ancho,self.alto=self.imagen.get_size()#tamaño pelota
        self.x=ventanaHor/2-self.ancho/2#posicionar y en el centro
        self.y=320#posicionar x en el centro
        self.dir_x=random.choice([-5,5])#direccion pelota eje x
        self.dir_y=random.choice([5,5])#direccion pelota eje y
        self.vidas=5

    def movimiento(self):
        self.x+=self.dir_x
        self.y+=self.dir_y
    
    def reinicio(self,raqueta):
        raqueta.reinicio()
        self.x=ventanaHor/2-self.ancho/2
        self.y=320

    def limpiar(self):
        self.vidas = 10
        self.reinicio()

    def rebotar(self,raqueta):

        if self.x<= -self.ancho:
            self.dir_x=-self.dir_x
            return True
        if self.x>= ventanaHor:
            self.dir_x=-self.dir_x
            return True
        if self.y<=0:
            self.dir_y=-self.dir_y  
            return False
        if self.y+self.alto>=ventanaVer:
            self.dir_y=-self.dir_y
            self.vidas -= 1
            self.reinicio(raqueta)
            return False
