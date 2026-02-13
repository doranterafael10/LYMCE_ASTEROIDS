from pathlib import Path
from pygame import mixer, mixer_music
from app.settings import GameSettings

class SoundManager:
    def __init__(self) -> None:
        self.sounds_dir: Path = GameSettings.SOUNDS_DIR
        self.music_dir: Path = GameSettings.MUSIC_DIR
        self._sounds = {}
        
    def _obtener_sonido(self, name: str) -> mixer.Sound:
        path = self.sounds_dir / f"{name}.mp3"
        if name not in self._sounds:
            self._sounds[name] = mixer.Sound(path)
        return self._sounds[name]
    
    def _obtener_pista(self, name: str) -> mixer_music:
        path = self.music_dir / f"{name}.mp3"
        return mixer_music.load(path)
    
    def play_efecto(self, name: str, volume: float = 1.0) -> None:
        sonido = self._obtener_sonido(name)
        sonido.set_volume(volume)
        sonido.play()
        
    def play_pista(self, name: str, volume: float = 1.0, loop: int = -1) -> None:
        pista = self.music_dir / f"{name}.mp3"
        mixer_music.load(str(pista))
        mixer_music.set_volume(volume)
        mixer_music.play(loop)
        
    def stop_pista(self) -> None:
        mixer_music.stop()
        
    def pause_pista(self) -> None:
        mixer_music.pause()
    
    def resume_pista(self) -> None:
        mixer_music.unpause()
        
        