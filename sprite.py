import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego con group")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Posición inicial del cuadrado que se mueve
x, y = 375, 275  # Centro de la pantalla
speed = 5  # Velocidad de movimiento

# Posición del cuadrado estático
static_x, static_y = 300, 200
static_size = 50  # Tamaño del cuadrado estático

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento del cuadrado que se mueve
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Detectar la colisión
    moving_rect = pygame.Rect(x, y, 50, 50)  # Rectángulo del cuadrado que se mueve
    static_rect = pygame.Rect(static_x, static_y, static_size, static_size)  # Rectángulo del cuadrado estático

    # Comprobamos si el cuadrado que se mueve colide con el cuadrado estático
    if moving_rect.colliderect(static_rect):
        print("¡Colisión detectada! El juego se cerrará.")
        pygame.quit()  # Cierra Pygame
        sys.exit()  # Sale del programa

    # Rellenar la pantalla con color negro
    screen.fill(BLACK)

    # Dibujar los cuadrados
    pygame.draw.rect(screen, WHITE, moving_rect)  # Cuadrado que se mueve
    pygame.draw.rect(screen, RED, static_rect)    # Cuadrado estático (rojo)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar los fotogramas por segundo (FPS)
    pygame.time.Clock().tick(60)