import pygame

class ElementEntity:
    def __init__(self, pos, vel):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)

    def update(self):
        self.pos += self.vel

    def draw(self, surface):
        pass