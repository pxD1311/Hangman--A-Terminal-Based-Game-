from random import choice
from hangman import Hangman


class Game:
    def __init__(self, words : list) -> None:
        self.words = words
        self.used_words = []
        self.game = None

    def _create_new_game(self) -> Hangman:
        if len(self.words): 
            selected_word = choice(self.words)
            self.used_words.append(selected_word)
            self.words.remove(selected_word)
            return Hangman(selected_word) 
        self.words = self.used_words
        self.used_words = []
        return self._create_new_game()

    def gameloop(self):
        play = 'y'
        while play in ('y', 'Y', 'Yes', 'YES', 'yes'):
            self.game = self._create_new_game()
            self.game.play_game()
            play = input("\t\t    Play again? (y/N):")
        print("\t\t    Thanks for playing!")