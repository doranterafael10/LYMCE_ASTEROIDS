from enum import Enum

class GameState(Enum):
    START = 1
    PLAYING = 2
    GAMEOVER = 3
    VICTORY = 4
    EASTER_EGG = 5
    INSTRUCTIONS = 6
    CREDITS = 7