import pygame
from app.settings.settings import WIDTH, HEIGHT, BLUE, GREEN, WHITE, RED, BLACK

class EasterEggHandler:
    def __init__(self):
        self.reset()
        self.font = pygame.font.SysFont("Courier", 20, bold=True)

    def reset(self):
        self.earth_y = HEIGHT + 450 
        self.show_screamer = False

    def update_and_draw(self, surface, asteroids):
        # Dibujar la Tierra
        pygame.draw.circle(surface, BLUE, (WIDTH // 2, int(self.earth_y)), 400)
        pygame.draw.circle(surface, GREEN, (WIDTH // 2 - 100, int(self.earth_y) - 50), 80)
        pygame.draw.circle(surface, GREEN, (WIDTH // 2 + 120, int(self.earth_y) + 30), 100)
        
        if self.earth_y > HEIGHT + 120: self.earth_y -= 0.8
            
        for a in asteroids:
            a.vel = pygame.Vector2(0, 1.2)
            a.update()
            a.draw(surface)
            if a.pos.y > self.earth_y - 380: self.show_screamer = True

        if self.show_screamer:
            surface.fill(RED)
            surface.blit(self.font.render("¡COLISIÓN GLOBAL!", True, BLACK), (WIDTH//2-100, HEIGHT//2))