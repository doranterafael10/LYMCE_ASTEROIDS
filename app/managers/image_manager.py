from pygame import image, Surface
from pathlib import Path

from app.settings import game_settings

class ImageManager:
    """
    Clase para la gestion de imagenes.
    """
    def __init__(self) -> None:
        self.images_dir: Path = game_settings.IMG_DIR
        self._images = {}

    def obtener_imagen(self, name: str) -> Surface
        """
        Obtiene una imagen del directorio de imagenes.

        Args:
            name (str): El nombre de la imagen a cargar.

        Returns:
        Surface: La superficie de la imagen cargada.
        """
        if name not in self._images:
           path = self.images_dir/ f"{name}.png"
           self._images[name] = image.load(path).convert_alpha()
        return self._images[name]
        