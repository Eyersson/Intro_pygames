#Importamos la libreria de pygame
import pygame
import random 
#inicializamos los modulos de pygame
pygame.init()

#establecer titulo ala ventana  
pygame.display.set_caption("Surface")

#establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

#definir un color
azul = random.randint(0,256)
amarillo = random.randint(0,256)
rojo = random.randint(0,256)
color_aleatorio=((azul,amarillo,rojo))

#crear una superficie

color_aleatorio = pygame.Surface((200,200))

#rellenamos la superficie de azul 
color_aleatorio.fill((azul,amarillo,rojo))

#muevo la superficie en la ventana 
ventana.blit(color_aleatorio, (100,100))

#actualizacion la visualizacion de la ventana
pygame.display.flip()

#bucle del juego

while True:
    event =pygame.event.wait()
    if event == pygame.QUIT:
        break

pygame.quit()