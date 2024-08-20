from random import choice
from hangman import Hangman


class Game:
    def __init__(self, words : dict[str, str]) -> None:
        self.words = words
        self.used_words = {}
        self.game = None

    def _create_new_game(self) -> Hangman:
        if len(self.words): 
            selected_word = choice(tuple(self.words.keys()))
            self.used_words[selected_word] = self.words[selected_word]
            word_description = self.words[selected_word]
            del self.words[selected_word]
            return Hangman(selected_word, word_description) 
        self.words = self.used_words
        self.used_words = []
        return self._create_new_game()

    def gameloop(self):
        play = 'y'
        while play not in ('n', 'N', 'NO', 'No', 'no', 'nO'):
            self.game = self._create_new_game()
            self.game.play_game()
            play = input("\t\t    Play again? (Y/n):")
        print("\t\t    Thanks for playing!")