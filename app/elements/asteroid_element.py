import pygame
import random
from app.settings.settings import WIDTH, HEIGHT, WHITE
from app.entities.elements_entity import ElementEntity

class Asteroid(ElementEntity):
    def __init__(self, pos=None, size=3, is_arepa=False, current_level=1):
        self.size = size
        self.is_arepa = is_arepa
        self.radius = 150 if is_arepa else size * 15
        
        # Determinar posición inicial
        pos = pygame.Vector2(pos) if pos else self.get_random_pos()
        
        # 1. Definición de la velocidad base según el rango de niveles solicitado
        if self.is_arepa:
            speed_mult = 0.5  # Velocidad para el Boss (Nivel 10)
        else:
            if 1 <= current_level <= 3:
                speed_mult = 0.6
            elif 4 <= current_level <= 5:
                speed_mult = 0.7
            elif 6 <= current_level <= 7:
                speed_mult = 0.8
            elif 8 <= current_level <= 9:
                speed_mult = 0.85
            else:
                speed_mult = 0.9  # Seguridad para niveles superiores

        # 2. Ajuste de proporción de tamaño (Pequeño x2 respecto al Grande)
        # Si size=3 (grande) -> multiplicador es 1.0 (velocidad base)
        # Si size=1 (pequeño) -> multiplicador es 2.0 (doble de velocidad)
        variacion_tamano = 1 + (3 - self.size) * 0.5
            
        # Cálculo de la velocidad vectorial final
        vel = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * speed_mult * variacion_tamano
        
        # Inicializar entidad base
        super().__init__(pos, vel)
        
        # Generar forma irregular del asteroide
        self.vertices = [pygame.Vector2(self.radius * random.uniform(0.8, 1.2), 0).rotate(i * 36) for i in range(10)]

    def get_random_pos(self):
        """Genera una posición aleatoria lejos del centro del mapa."""
        p = pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        while p.distance_to(pygame.Vector2(WIDTH//2, HEIGHT//2)) < 150:
            p = pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        return p

    def update(self):
        """Actualiza posición y maneja el rebote/teletransporte en bordes."""
        super().update()
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

    def draw(self, surface):
        """Dibuja el asteroide (normal o jefe final)."""
        if self.is_arepa:
            cx, cy = int(self.pos.x), int(self.pos.y)
            pygame.draw.circle(surface, WHITE, (cx, cy), self.radius, 2)
            for i in range(-100, 101, 40):
                pygame.draw.line(surface, WHITE, (cx-80, cy+i), (cx+80, cy+i), 1)
        else:
            pts = [self.pos + v for v in self.vertices]
            pygame.draw.polygon(surface, WHITE, pts, 2)