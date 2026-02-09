import pygame
from app.enums.game_state_enum import GameState

class CheatManager:
    def __init__(self, code="lymce"):
        self.code = code.lower()
        self.buffer = ""
        self.flash_active = False
        self.flash_timer = 0

    def check_key(self, event, current_state):
        if event.type == pygame.KEYDOWN and current_state == GameState.PLAYING:
            char = event.unicode.lower()
            if char.isalpha():
                self.buffer += char
                self.buffer = self.buffer[-len(self.code):]
            if self.code in self.buffer:
                self.buffer = ""
                self.flash_active = True
                self.flash_timer = 200
                return True
        return False

    def update_flash(self, dt):
        if self.flash_timer > 0:
            self.flash_timer -= dt
        else:
            self.flash_active = False