import sys
import os

# Permite importar desde las subcarpetas de app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.engine import GameEngine

def main():
    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
    