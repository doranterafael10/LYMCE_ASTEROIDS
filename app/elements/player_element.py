import pygame
from app.settings.settings import WIDTH, HEIGHT, WHITE
from app.entities.elements_entity import ElementEntity

class Player(ElementEntity):
    def __init__(self):
        super().__init__((WIDTH // 2, HEIGHT // 2), (0, 0))
        self.lives = 3
        self.score = 0
        self.angle = 0
        self.points = [[0, -15], [-10, 15], [0, 10], [10, 15]]

    def reset(self):
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
        self.vel = pygame.Vector2(0, 0)
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.angle += 5
        if keys[pygame.K_RIGHT]: self.angle -= 5
        if keys[pygame.K_UP]:
            acc = pygame.Vector2(0, -0.2).rotate(-self.angle)
            self.vel += acc
        super().update() # Usa el movimiento de la entidad base
        self.vel *= 0.99
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

    def draw(self, surface):
        rotated_pts = [self.pos + pygame.Vector2(p).rotate(-self.angle) for p in self.points]
        pygame.draw.polygon(surface, WHITE, rotated_pts, 2)