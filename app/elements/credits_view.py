import pygame
from app.settings.settings import WIDTH, WHITE, BLUE, RED

class CreditsView:
    def __init__(self, font):
        self.font = font

    def draw(self, surface):
        surface.blit(self.font.render("=== CREDITOS ===", True, BLUE), (WIDTH//2-80, 200))
        surface.blit(self.font.render("DESARROLLADO POR: L-Y-M-C-E", True, WHITE), (WIDTH//2-140, 280))
        surface.blit(self.font.render("MOTOR GRAFICO: PYGAME", True, WHITE), (WIDTH//2-110, 320))
        surface.blit(self.font.render("PULSA [ESC] PARA VOLVER", True, RED), (WIDTH//2-110, 450))