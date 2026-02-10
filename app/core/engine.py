import pygame
import os
import random
from app.settings import GameColors, GameSettings
from app.enums import GameState
from app.core.cheat_manager import CheatManager
from app.elements import (
    InstructionsView,
    CreditsView,
    EasterEggHandler,
    Bullet,
    Asteroid,
    Player
)

class GameEngine:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        self.screen = pygame.display.set_mode((GameSettings.WIDTH, GameSettings.HEIGHT))
        pygame.display.set_caption("ASTEROIDS 1.0")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Courier", 20, bold=True)
        
        # Inicialización de módulos externos
        self.instructions_screen = InstructionsView(self.font)
        self.credits_screen = CreditsView(self.font)
        self.cheats = CheatManager("lymce")
        self.easter_egg = EasterEggHandler()
        
        self.running = True
        self.game_state = GameState.START 
        
        if os.path.exists(GameSettings.FILE_MUSIC):
            try:
                pygame.mixer.music.load(GameSettings.FILE_MUSIC)
                pygame.mixer.music.play(-1)
            except: pass
        self.reset_game_logic()

    def reset_game_logic(self):
        """Limpia el estado del juego para una nueva partida."""
        self.player = Player()
        self.asteroids = [Asteroid(current_level=1) for _ in range(5)]
        self.bullets = []
        self.level = 1
        self.jump_cooldown = 0
        self.boss_health = 100
        self.inactivity_timer = 0
        self.easter_egg.reset()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # 1. Verificar Truco Secreto (LYMCE)
                if self.cheats.check_key(event, self.game_state):
                    self.level = 10
                    self.asteroids = [Asteroid(is_arepa=True, current_level=10)]
                    self.boss_health = 100
                    self.bullets = []

                # 2. Navegación en Menú de Inicio
                if self.game_state == GameState.START:
                    if event.key == pygame.K_SPACE:
                        self.reset_game_logic()
                        self.game_state = GameState.PLAYING
                    elif event.key == pygame.K_i: 
                        self.game_state = GameState.INSTRUCTIONS
                    elif event.key == pygame.K_c: 
                        self.game_state = GameState.CREDITS
                
                # 3. Salir de submenús o pantallas de fin
                elif self.game_state in [GameState.INSTRUCTIONS, GameState.CREDITS, GameState.GAMEOVER, GameState.VICTORY]:
                    if event.key in [pygame.K_ESCAPE, pygame.K_SPACE]:
                        self.game_state = GameState.START

                # 4. Controles durante la partida
                elif self.game_state == GameState.PLAYING:
                    # DISPARO CORREGIDO: Funciona en todos los niveles (incluyendo el 10)
                    if event.key == pygame.K_SPACE:
                        self.bullets.append(Bullet(self.player.pos, self.player.angle))
                    
                    # Teletransporte (Solo nivel 5 o más)
                    if self.level >= 5 and event.key == pygame.K_LSHIFT:
                        if self.jump_cooldown <= 0:
                            self.player.pos = pygame.Vector2(random.randint(0, GameSettings.WIDTH), random.randint(0, GameSettings.HEIGHT))
                            self.jump_cooldown = 2000

    def update(self, dt):
        # Actualizar efectos de trucos (flash verde)
        self.cheats.update_flash(dt)
        
        if self.game_state == GameState.PLAYING:
            self.player.update()
            if self.jump_cooldown > 0: self.jump_cooldown -= dt
            
            # Control de inactividad para Easter Egg
            keys = pygame.key.get_pressed()
            if not any([keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_SPACE]]):
                self.inactivity_timer += dt
            else: self.inactivity_timer = 0
            if self.inactivity_timer > 10000: self.game_state = GameState.EASTER_EGG

            # Actualizar balas
            for b in self.bullets[:]:
                b.update()
                if b.timer <= 0: self.bullets.remove(b)

            # Actualizar asteroides y colisiones
            for a in self.asteroids[:]:
                a.update()
                
                # Colisión Jugador - Asteroide
                if self.player.pos.distance_to(a.pos) < a.radius + 10:
                    self.player.lives -= 1
                    self.player.reset()
                    if self.player.lives <= 0:
                        self.game_state = GameState.GAMEOVER

                # Colisión Bala - Asteroide
                for b in self.bullets[:]:
                    if b.pos.distance_to(a.pos) < a.radius:
                        if b in self.bullets: self.bullets.remove(b)
                        
                        if self.level == 10: # Lógica especial para el Boss
                            self.boss_health -= 1
                            if self.boss_health <= 0:
                                self.asteroids.remove(a)
                                self.game_state = GameState.VICTORY
                        else: # Lógica para niveles normales
                            self.player.score += 10
                            if a.size > 1:
                                self.asteroids.append(Asteroid(a.pos, a.size-1, current_level=self.level))
                                self.asteroids.append(Asteroid(a.pos, a.size-1, current_level=self.level))
                            self.asteroids.remove(a)
                        break

            # Cambio de nivel
            if not self.asteroids and self.level < 10:
                self.level += 1
                num_asteroids = 1 if self.level == 10 else 5 + self.level
                self.asteroids = [Asteroid(is_arepa=(self.level==10), current_level=self.level) for _ in range(num_asteroids)]

    def draw(self):
        # Dibujar fondo (o flash de truco)
        if self.cheats.flash_active:
            self.screen.fill(GameColors.GREEN)
        else:
            self.screen.fill(GameColors.BLACK)

        if self.game_state == GameState.PLAYING:
            self.player.draw(self.screen)
            for a in self.asteroids: a.draw(self.screen)
            for b in self.bullets: b.draw(self.screen)
            ui_text = f"SCORE: {self.player.score}  LVL: {self.level}  LIVES: {self.player.lives}"
            self.screen.blit(self.font.render(ui_text, True, GameColors.WHITE), (10, 10))
            if self.level == 10:
                boss_txt = f"BOSS HP: {self.boss_health}"
                self.screen.blit(self.font.render(boss_txt, True, GameColors.RED), (GameColors.WIDTH//2-60, 40))
        
        elif self.game_state == GameState.START:
            self.screen.blit(self.font.render(f"{GameSettings.GAME_NAME} - {GameSettings.GAME_VERSION}", True, GameColors.WHITE), (GameSettings.WIDTH//2-70, GameSettings.HEIGHT//2-120))
            self.screen.blit(self.font.render("INICIAR JUEGO [ESPACIO]", True, GameColors.WHITE), (GameSettings.WIDTH//2-120, GameSettings.HEIGHT//2 - 20))
            self.screen.blit(self.font.render("INSTRUCCIONES [I]", True, GameColors.WHITE), (GameSettings.WIDTH//2-120, GameSettings.HEIGHT//2 + 30))
            self.screen.blit(self.font.render("CREDITOS      [C]", True, GameColors.WHITE), (GameSettings.WIDTH//2-120, GameSettings.HEIGHT//2 + 80))

        elif self.game_state == GameState.INSTRUCTIONS:
            self.instructions_screen.draw(self.screen)
            
        elif self.game_state == GameState.CREDITS:
            self.credits_screen.draw(self.screen)
            
        elif self.game_state == GameState.GAMEOVER:
            self.screen.blit(self.font.render("GAME OVER - PULSA ESPACIO PARA MENU", True, GameColors.WHITE), (GameSettings.WIDTH//2-180, GameSettings.HEIGHT//2))
            
        elif self.game_state == GameState.VICTORY:
            self.screen.blit(self.font.render("¡VICTORIA! - PULSA ESPACIO PARA MENU", True, GameColors.WHITE), (GameSettings.WIDTH//2-180, GameSettings.HEIGHT//2))
            
        elif self.game_state == GameState.EASTER_EGG:
            self.easter_egg.update_and_draw(self.screen, self.asteroids)

    def run(self):
        while self.running:
            dt = self.clock.tick(GameSettings.FPS)
            self.handle_events()
            self.update(dt)
            self.draw()
            pygame.display.flip()
        pygame.quit()