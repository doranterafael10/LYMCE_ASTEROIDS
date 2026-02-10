from abc import ABC, abstractmethod
from pygame import Vector2, Surface

class ElementEntity(ABC):
    def __init__(self, pos, vel):
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)

@abstractmethod
def update(self):
    """
    Metodo abstracto para actualizar la posicion de la entidad.
    """   
    self.pos += self.vel

@abstractmethod
def draw(self, surface: Surface):
    """
    Metodo abstracto para dibujar la entidad en una superficie.
    """  
    pass