import pygame
import sys

pygame.init()

Negro = (0, 0, 0)
Morado = (191, 64, 191)
blanco = (255, 255, 255)
verde = (0,255,0)
azul = (0,0,255)
azul1 = (0, 107, 255)
rojo = (195, 15, 15)
gris = (175, 115, 115)
amarillo1 = (233, 221, 41)
grisclaro = (197, 188, 173)
cafe = (153, 113, 50)
grisnegro = (77, 76, 75)
rosa = (252, 167, 247)
azuloscuro = (7, 5, 69)
azulclaro = (145, 255, 217)


ventana = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Lineas Randoms")

clock = pygame.time.Clock()



while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

#   Sistemas De Rectangulo 
    pygame.draw.rect(ventana, Negro, (100, 120, 600, 530), 1)

#   Crear lineas aleatorias
#
  
#  Sistemas de texto.
    fuente_arial = pygame.font.SysFont("Arial", 30,1,1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1, grisnegro)
    ventana.blit(texto,(35,30))
    
    fuente_arial = pygame.font.SysFont("Arial", 30,1,1)
    texto = fuente_arial.render("Chelo:)", 1 ,Negro)
    ventana.blit(texto,(105,120, ))


    fuente_arial = pygame.font.SysFont("Arial", 20,1,0)
    texto = fuente_arial.render("Especialidad Sistemas", 1, Negro)
    ventana.blit(texto,(150,70))

    fuente_arial = pygame.font.SysFont("Arial", 12,1,0)
    texto = fuente_arial.render("Estudiante de 10-4", 1, Negro)
    ventana.blit(texto,(10,10))

    pygame.draw.rect(ventana, amarillo1, (400,160, 200, 30))
    pygame.draw.rect(ventana, amarillo1, (380,190, 240, 30))
    pygame.draw.rect(ventana, Morado, (400,220, 200, 150))
    pygame.draw.rect(ventana, grisclaro, (430,245, 140, 110))
    pygame.draw.circle(ventana, Morado, (230, 440), 50)
    pygame.draw.circle(ventana, rosa, (500, 300), 50)
    pygame.draw.circle(ventana, blanco, (480, 290), 15)
    pygame.draw.circle(ventana, blanco, (520, 290), 15)
    pygame.draw.circle(ventana, amarillo1, (500, 320), 10)
    pygame.draw.circle(ventana, gris, (520, 290), 7)
    pygame.draw.circle(ventana, gris, (480, 290), 7)
    pygame.draw.line(ventana, Morado, (470, 260), (495, 275), 4)
    pygame.draw.line(ventana, Morado, (525, 260), (500, 275), 4)
    pygame.draw.rect(ventana, grisnegro, (260,370, 360, 150))
    pygame.draw.circle(ventana, cafe , (590, 520), 50)
    pygame.draw.circle(ventana, cafe, (450, 520), 50)
    pygame.draw.circle(ventana, cafe, (310, 520), 50)
    pygame.draw.rect(ventana, Negro, (335,510, 100, 30))
    pygame.draw.rect(ventana, Negro, (480,510, 100, 30))
    pygame.draw.rect(ventana, azuloscuro, (240,390, 20, 100))
    pygame.draw.rect(ventana, azuloscuro, (210,360, 30, 150))
    pygame.draw.rect(ventana, Morado, (290,300, 50, 70))
    pygame.draw.rect(ventana, grisnegro, (270,270, 90, 30))
    

  
    pygame.display.flip()



