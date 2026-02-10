from pathlib import Path

___version___ = "0.0.0"

class GameSettings:
    # Informacion sobre el juego
    GAME_NAME: str = "ASTEROIDS"
    GAME_VERSION: str = ___version___
    
    # Informacion sobre la pantalla
    WIDTH: int = 800
    HEIGHT: int = 600
    FPS: int = 60
    
    # Musica
    FILE_MUSIC = "musica.mp3"