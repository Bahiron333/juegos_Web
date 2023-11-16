import pygame
import pygame.locals
import sys

class Pregunta():

    def __init__(self,ventana):

        #ventana de fondo
        self.ventana = ventana
        self.text_question =[] #texto de la pregunta
        self.font = pygame.font.SysFont('arial',33,bold=False)#Fuente de texto
        self.font_opciones= pygame.font.SysFont('arial',15,bold=False)
        self.respuesta = ""#respuesta correcta de la pregunta
        self.ubicacion_text_y = 0
        self.ubicacion_text_x = 0
        self.preguntas_contestada = False#si la pregunta fue contestada
        self.pregunta_correcto = False#si la opcion escogida fue correcta
        self.rectangulo_pregunta = pygame.Rect(250,30,500,500)#fondo de las preguntas
        self.rectangulo_mostrar_pregunta = pygame.Rect(255,35,490,400)#fondo texto pregunta

        #texto de botones
        self.A = ""
        self.B = ""
        self.C = ""
        self.D = ""
    
        self.boton_A= pygame.Rect(255,445,240,30)
        self.boton_B= pygame.Rect(255,485,240,30)
        self.boton_C= pygame.Rect(505,445,240,30)
        self.boton_D= pygame.Rect(505,485,240,30)

    def escoger_pregunta(self,num,vida):

        self.num_pregunta = num
        #Pregunta 1
        if self.num_pregunta == 1:
            self.text_question.append("¿A qué velocidad debe circular")
            self.text_question.append("un auto de carreras para recorrer")
            self.text_question.append("50km en un cuarto de hora?")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 300
            self.A = "200 km"
            self.B = "100 km"
            self.C = "150 km"
            self.D = "250 km"
            self.respuesta = "200 km"
        #Pregunta 2
        elif self.num_pregunta == 2:
            self.text_question.append("Una bicicleta circula en línea recta")
            self.text_question.append("a una velocidad de 15km/h durante")
            self.text_question.append("45 minutos. ¿Qué distancia recorre?")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 280
            self.A = "11,96 km"
            self.B = "11,12 km"
            self.C = "11,47 km"
            self.D = "11,25 km"
            self.respuesta = "11,25 km"

        #Pregunta 3
        elif self.num_pregunta == 3:
            self.text_question.append("Si Alberto recorre con su patinete")
            self.text_question.append("una pista de 300 metros en un ")
            self.text_question.append("minuto, ¿a qué velocidad circula?")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 300
            self.A = "3 m/s"
            self.B = "6 m/s"
            self.C = "5 m/s"
            self.D = "7 m/s"
            self.respuesta = "5 m/s"

        #Preguntas 4
        elif self.num_pregunta == 4:
            self.text_question.append("¿Cuántos metros recorre una")
            self.text_question.append("motocicleta en un segundo si")
            self.text_question.append("circula a una velocidad de 90")
            self.text_question.append("km/h?")
            self.ubicacion_text_y = 150
            self.ubicacion_text_x= 320
            self.A = "19 m/s"
            self.B = "25 m/s"
            self.C = "47 m/s"
            self.D = "53 m/s"
            self.respuesta = "25 m/s"

        #Pregunta 5
        elif self.num_pregunta == 5:
            self.text_question.append("Si un avión tarda 2 segundos")
            self.text_question.append("en recorrer 160 metros,")
            self.text_question.append("¿cuál es su velocidad en km/h?")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 310
            self.A = "300 km/h"
            self.B = "274 km/h"
            self.C = "312 km/h"
            self.D = "288 km/h"
            self.respuesta = "288 km/h"

        #pregunta 6
        elif self.num_pregunta == 6:
            self.text_question.append("Sabiendo que la velocidad del sonido")
            self.text_question.append("es de 343,2 m/s, ¿a cuántos kilómetro ")
            self.text_question.append("de distancia se produce un trueno")
            self.text_question.append("que tarda 6 segundos en oírse?")
            self.ubicacion_text_y = 140
            self.ubicacion_text_x= 270
            self.A = "2,1562 km"
            self.B = "2,8542 km"
            self.C = "2,0592 km"
            self.D = "2,1423 km"
            self.respuesta = "2,0592 km"

        #Pregunta 7
        elif self.num_pregunta == 7:
            self.text_question.append("La velocidad de la luz en el vacío es,")
            self.text_question.append("aproximadamente, c=300.000 km/s.")
            self.text_question.append("¿Cuánto tarda en llegar la luz del Sol")
            self.text_question.append("al planeta Tierra si éstos distan ")
            self.text_question.append("unos 149,6 millones de kilómetros?")
            self.ubicacion_text_y = 110
            self.ubicacion_text_x= 275
            self.A = "8,123 min"
            self.B = "8,311 min"
            self.C = "8,189 min"
            self.D = "8,19 min"
            self.respuesta = "8,311 min"

        #Pregunta 8
        elif self.num_pregunta == 8:
            self.text_question.append("Calculadora del producto")
            self.text_question.append("escalar de dos vectores")
            self.text_question.append("v=(6,2) y w=(8,2)")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 350
            self.A = "52"
            self.B = "40"
            self.C = "23"
            self.D = "30"
            self.respuesta = "52"

        #pregunta 9
        elif self.num_pregunta == 9:
            self.text_question.append("Calculadora del módulo de")
            self.text_question.append("un vector v=(9,3) de R2")
            self.ubicacion_text_y = 180
            self.ubicacion_text_x= 340
            self.A = "√180"
            self.B = "√9"
            self.C = "√27"
            self.D = "√90"
            self.respuesta = "√90"

        #pregunta 10
        elif self.num_pregunta == 10:
            self.text_question.append("Calcular la distancia entre los")
            self.text_question.append("siguientes dos puntos del plano:")
            self.text_question.append("A=(-1,-1), B=(1,1)")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 310
            self.A = "2√8"
            self.B = "2√4"
            self.C = "2√2"
            self.D = "2√16"
            self.respuesta = "2√2"

        #pregunta 11
        elif self.num_pregunta == 11:
            self.text_question.append("Calcular los dos vectores que unen")
            self.text_question.append("a los puntos A y B dados por:")
            self.text_question.append("A=(2,-1) B=(-1,2)")
            self.ubicacion_text_y = 160
            self.ubicacion_text_x= 290
            self.A = "(-3,3) (3,-3)"
            self.B = "(-3,3) (-3,3)"
            self.C = "(-3,-3) (3,3)"
            self.D = "(3,3) (-3,-3)"
            self.respuesta = "(-3,3) (3,-3)"
        
        #pregunta 12
        elif self.num_pregunta == 12:
            self.text_question.append("Calculadora del producto escalar")
            self.text_question.append("de dos vectores v=(4,3) y w=(2,5)")
            self.ubicacion_text_y = 180
            self.ubicacion_text_x= 290
            self.A = "23"
            self.B = "24"
            self.C = "25"
            self.D = "26"
            self.respuesta = "23"

        #pregunta 13
        elif self.num_pregunta == 13:
            self.text_question.append("Calculadora del módulo de")
            self.text_question.append("un vector v=(5,25) de R2")
            self.ubicacion_text_y = 180
            self.ubicacion_text_x= 340
            self.A = "√650"
            self.B = "√150"
            self.C = "√25"
            self.D = "√5"
            self.respuesta = "√650"

        #pregunta 14
        elif self.num_pregunta == 14:
            self.text_question.append("Calculadora del producto escalar")
            self.text_question.append("de dos vectores v=(7,8) y w=(4,2)")
            self.ubicacion_text_y = 180
            self.ubicacion_text_x= 290
            self.A = "36"
            self.B = "41"
            self.C = "44"
            self.D = "47"
            self.respuesta = "44"

        ##pregunta 15
        elif self.num_pregunta == 15:
            self.text_question.append("Calculadora del módulo ")
            self.text_question.append("de un vector v=(2,8) de R2")
            self.ubicacion_text_y = 180
            self.ubicacion_text_x= 340
            self.A = "√64"
            self.B = "√68"
            self.C = "√60"
            self.D = "√16"
            self.respuesta = "√68"

        self.mostrar_pregunta(vida)


    def mostrar_pregunta(self,vida):
   
        while  self.preguntas_contestada != True:
            pygame.draw.rect(self.ventana,(225,225,225),self.rectangulo_pregunta)
            pygame.draw.rect(self.ventana,(0,0,0),self.rectangulo_mostrar_pregunta)
            
            #Agregando botones de opciones
            pygame.draw.rect(self.ventana,(0,0,0),self.boton_A)
            pygame.draw.rect(self.ventana,(0,0,0),self.boton_B)
            pygame.draw.rect(self.ventana,(0,0,0),self.boton_C)
            pygame.draw.rect(self.ventana,(0,0,0),self.boton_D)
            #creando texto boton
            letrero_A = self.font_opciones.render("A. "+self.A,True,(255,255,255))
            letrero_B = self.font_opciones.render("B. "+self.B,True,(255,255,255))
            letrero_C = self.font_opciones.render("C. "+self.C,True,(255,255,255))
            letrero_D = self.font_opciones.render("D. "+self.D,True,(255,255,255))
            #Añadiendo texto boton
            self.ventana.blit(letrero_A,(self.boton_A.x+10,self.boton_A.y+5))
            self.ventana.blit(letrero_B,(self.boton_B.x+10,self.boton_B.y+5))
            self.ventana.blit(letrero_C,(self.boton_C.x+10,self.boton_C.y+5))
            self.ventana.blit(letrero_D,(self.boton_D.x+10,self.boton_D.y+5))


            #Añadimos las lineas de texto a ventana
            ubicacion_y = self.ubicacion_text_y #reiniciamos para que no se repita
            for texto in self.text_question:
                    texto_pregunta = self.font.render(texto,True,('white'))
                    self.ventana.blit(texto_pregunta,(self.ubicacion_text_x,ubicacion_y))
                    ubicacion_y += 50


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_A.collidepoint(event.pos):
                        if self.A == self.respuesta:
                            self.pregunta_correcto=True
                            vida.vidas+=1
                        else:
                            self.pregunta_correcto=False
                            
                        self.preguntas_contestada=True
                        self.main_mostrar_resultado()
                    if self.boton_B.collidepoint(event.pos):
                        if self.B == self.respuesta:
                            self.pregunta_correcto=True
                            vida.vidas+=1
                        else:
                            self.pregunta_correcto=False
                        self.preguntas_contestada=True
                        self.main_mostrar_resultado()
                    if self.boton_C.collidepoint(event.pos):
                        if self.C == self.respuesta:
                            self.pregunta_correcto=True
                            vida.vidas+=1
                        else:
                            self.pregunta_correcto=False
                        self.preguntas_contestada=True  
                        self.main_mostrar_resultado()                      
                    if self.boton_D.collidepoint(event.pos):
                        if self.D == self.respuesta:
                            self.pregunta_correcto=True
                            vida.vidas+=1
                        else:
                            self.pregunta_correcto=False
                        self.preguntas_contestada=True
                        self.main_mostrar_resultado()
                                        
            pygame.display.update()

    def main_mostrar_resultado(self):

        font_res = pygame.font.SysFont("harrington",60,bold=False)

        boton_aceptar =pygame.Rect(420,450,150,65)
        visto = True

        while visto:

            #Agregando botones de opciones

            if self.pregunta_correcto:
                letrero = font_res.render("!Correcto¡",True,(255,255,255))
                pygame.draw.rect(self.ventana,(225,225,225),self.rectangulo_pregunta)
                pygame.draw.rect(self.ventana,(0,0,0),self.rectangulo_mostrar_pregunta)
                self.ventana.blit(letrero,(370,190))
                
            else: 
                letrero = font_res.render("Incorrecto",True,(255,255,255))
                pygame.draw.rect(self.ventana,(225,225,225),self.rectangulo_pregunta)
                pygame.draw.rect(self.ventana,(0,0,0),self.rectangulo_mostrar_pregunta)
                self.ventana.blit(letrero,(370,190))
           
            pygame.draw.rect(self.ventana,(0,0,0),boton_aceptar)

            #texto boton
            font_aceptar = pygame.font.SysFont("arial",30,bold=False)
            letrero_aceptar = font_aceptar.render("Aceptar",True,(255,255,255))
            self.ventana.blit(letrero_aceptar,(boton_aceptar.x+32,boton_aceptar.y+12))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_aceptar.collidepoint(event.pos):
                        visto = False


            pygame.display.update()
