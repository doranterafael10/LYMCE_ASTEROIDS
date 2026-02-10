from enum import IntEnum

class GameState(IntEnum):
    """
    Enum para representar los estados del juego.
    """
    START = 1
    PLAYING = 2
    GAMEOVER = 3
    VICTORY = 4
    EASTER_EGG = 5
    INSTRUCTIONS = 6
    CREDITS = 7

    def ___str___(self):
        return self.name