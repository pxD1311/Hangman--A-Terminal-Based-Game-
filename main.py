from game import Game
from words import get_word_dict

game = Game(get_word_dict())
game.gameloop()