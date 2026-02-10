from pathlib import Path

___version___ = "0.0.1"

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
    
    # Directorios
    DIR_BASE = Path(__file__).resolve().parent.parent
    ASSETS_DIR: Path = DIR_BASE / "assets"
    IMG_DIR: Path = ASSETS_DIR / "img"
    SOUNDS_DIR: Path = ASSETS_DIR / "sounds"
    MUSIC_DIR: Path = ASSETS_DIR / "ost"
    
    DIRS = [ASSETS_DIR, IMG_DIR, SOUNDS_DIR, MUSIC_DIR]
    for d in DIRS:
        d.mkdir(exist_ok=True)