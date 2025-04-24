import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego con sprite")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase para el cuadrado que se mueve
class MovingSquare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Crea una superficie para el cuadrado
        self.image.fill(WHITE)  # Rellena la superficie con color blanco
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 275
        self.speed = 5  # Velocidad de movimiento

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        
        # Movimiento del cuadrado
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Crear el grupo de sprites
all_sprites = pygame.sprite.Group()

# Crear la instancia del cuadrado que se mueve
moving_square = MovingSquare()

# Agregar el cuadrado al grupo de sprites
all_sprites.add(moving_square)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar todos los sprites
    all_sprites.update()

    # Rellenar la pantalla con color negro
    screen.fill(BLACK)

    # Dibujar todos los sprites
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar los fotogramas por segundo (FPS)
    pygame.time.Clock().tick(60)