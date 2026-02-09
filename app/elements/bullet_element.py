import pygame
from app.settings.settings import WHITE
from app.entities.elements_entity import ElementEntity

class Bullet(ElementEntity):
    def __init__(self, pos, angle):
        vel = pygame.Vector2(0, -10).rotate(-angle)
        super().__init__(pos, vel)
        self.timer = 50

    def update(self):
        super().update()
        self.timer -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.pos.x), int(self.pos.y)), 2)