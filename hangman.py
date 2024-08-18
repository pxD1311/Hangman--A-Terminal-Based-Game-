import platform
from os import system

class Hangman:
    def __init__(self, word) -> None:
        self.word = word
        self.player_guess : str
        self.player_progress = ["_"]*len(self.word)
        self.tries = 7
        self.clear_command = self._get_clear_command()

    def play_game(self) -> None:
        self._display_starting_text()

        while self.tries > 0:
            self._draw_screen()
            if self._winCheck(self._inputTerminal()):
                self._display_winning_text()
                break
        else:
            self._display_losing_text()

    def _draw_hangman(self, size : int) -> None:
        size = size if size > 3 else 4
        height = int(size/2)

        print("\n")
        print("="*30)

        for i in range(4):
            print(f"||\t\t{' '*(height+1)} |")

        if self.tries <= 6:
            self._draw_head(height)

        if self.tries <= 5:
            self._draw_body(height)

        if self.tries == 4:
            self._draw_one_arm(height)

        elif self.tries <= 3:
            self._draw_both_arms(height)

        if self.tries == 2:
            self._draw_one_leg(height)

        elif self.tries <= 1:
            self._draw_both_legs(height)

        print("||\n"*height,end='||')
        print("="*50)

    @staticmethod
    def _draw_head(height : int) -> None:
        head = ["    * *", " *       *", "*         *", " *       *", "    * *"] if height >= 3 else   ["    *", " *     *", "*       *", " *     *", "    *"]

        for i in head:
            print(f"||\t\t{' '*(height-3)}{i}")

    @staticmethod
    def _draw_body(height : int) -> None:
        print(f"||\t\t{' '*(height+1)} *\n"*int(height),end = '')

    @staticmethod
    def _draw_one_arm(height : int) -> None:
        for i in range(height):
            print(f"||\t\t{' '*(height-i)}*{' '*i} *")
        print(f"||\t\t{' '*(height+1)} *\n"*height, end = '')

    @staticmethod
    def _draw_both_arms(height : int) -> None:
        for i in range(height):
            print(f"||\t\t{' '*(height-i)}*{' '*i} *{' '*i} *")
        print(f"||\t\t{' '*(height+1)} *\n"*height, end = '')

    @staticmethod
    def _draw_one_leg(height : int) -> None:
        for i in range(height):
            print(f"||\t\t{' '*(height-i)}*{' '*i}")

    @staticmethod
    def _draw_both_legs(height : int) -> None:
        for i in range(height):
            print(f"||\t\t{' '*(height-i)}*{' '*i}  {' '*i} *")

    def _display_starting_text(self) -> None:
        print(f"""\t\tWelcome to Hang-Man !! Guess a given word in {self.tries} tries!!
\t\tIf you fail to do so then poor Johnny will be hanged to death!!
\t\tDo you have what it takes to save poor Johnny?
\t\tTime to find out!""")
        input("\t\tPress enter to begin!")

    def _draw_screen(self) -> None:
        system(self.clear_command)
        self._draw_hangman(6)
        print("\t\t",*self.player_progress, sep = " ")
        print(f"\t\tTries left : {self.tries}")

    @staticmethod
    def _display_winning_text() -> None:
        print("\t\tYOU ACTUALLY SAVED LIL JOHNNY!!!\n\t\t\tCONGRATULATINS!!\n\t\t\t    YOU WON")

    @staticmethod
    def _display_losing_text() -> None:
        print("\t\tYOU FAILED!! NOW JOHNNY HAS BEEN HANGED TO DEATH ALL CUZ OF YOU!!")
        print("\t\t\t\t    SHAME ON YOU LOSER!!!")

    def _is_character(self) -> bool:
        if self.player_guess is not None:
            return True if len(self.player_guess) == 1 else False
        print("No player input yet")
        return None

    def _inputTerminal(self) -> dict[str, bool]:
        self.player_guess = input("Enter your guess :")
        return {"guess" : self.player_guess,"is_char" : self._is_character()}

    def _update_progress(self, letter : str) -> bool:
        for i, char in enumerate(self.word):
            if char == letter:
                self.player_progress[i] = letter
                return True
        return False

    def _winCheck(self, input : dict[str, bool]) -> bool:
        if input["is_char"] and self._update_progress(input["guess"]):
            if  self.player_progress == [i for i in self.word]:
                return True
        elif not input["is_char"] and input["guess"] == self.word:
            return True
        else:    
            self.tries -= 1
            return False

    @staticmethod
    def _get_clear_command() -> str:
        os_name = platform.system()
        if os_name in ("Linux", "Darwin"):
            return "clear"
        elif os_name == "Windows":
            return "cls"
        else:
            return ValueError(f"Unsupported operating system : {os_name}")
