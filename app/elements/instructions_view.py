import pygame
from app.settings.settings import WIDTH, WHITE, GREEN, RED

class InstructionsView:
    def __init__(self, font):
        self.font = font

    def draw(self, surface):
        surface.blit(self.font.render("=== INSTRUCCIONES ===", True, GREEN), (WIDTH//2-110, 150))
        surface.blit(self.font.render("FLECHAS: MOVERSE Y ROTAR", True, WHITE), (WIDTH//2-130, 220))
        surface.blit(self.font.render("ESPACIO: DISPARAR", True, WHITE), (WIDTH//2-130, 260))
        surface.blit(self.font.render("L-SHIFT: TELETRANSPORTE (LVL 5+)", True, WHITE), (WIDTH//2-170, 300))
        surface.blit(self.font.render("PULSA [ESC] PARA VOLVER", True, RED), (WIDTH//2-110, 450))