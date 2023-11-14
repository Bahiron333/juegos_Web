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
        self.y=ventanaVer/2-self.alto/2#posicionar x en el centro
        self.dir_x=random.choice([-6,6])#direccion pelota eje x
        self.dir_y=random.choice([-6,6])#direccion pelota eje y
        self.puntuacion = 3#puntuacion humano
        self.resultado = ""
        self.final_juego=False

    def movimiento(self):
        self.x+=self.dir_x
        self.y+=self.dir_y

    def get_final(self):
        return self.final_juego
    
    def set_final(self,fin):
        self.final_juego = fin

    def reinicio(self):
        self.x=ventanaHor/2-self.ancho/2
        self.y=ventanaVer/2-self.alto/2
        self.dir_x=self.dir_x
        self.dir_y=random.choice([-5,5])


    def limpiar(self):
        self.puntuacion=0
        self.puntuacion_maqui=0
        self.reinicio()

    def get_resultado(self):
        return self.resultado
    
    def get_nombre_ganador(self):
        try:
            return self.nombre_ganador
        except:
            pygame.quit()
            sys.exit()
        
    
    def rebotar(self):
        if self.x<= -self.ancho:
            self.dir_x=-self.dir_x
            return True
        if self.x>= ventanaHor:
            self.puntuacion+=1
            self.dir_x=-self.dir_x
            return True
        if self.y<=0:
            self.dir_y=-self.dir_y     
            return False
        if self.y+self.alto>=ventanaVer:
            self.dir_y=-self.dir_y
            return False
