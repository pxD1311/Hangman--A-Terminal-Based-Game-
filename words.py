import os
from csv import reader

def __get_words_from_csv(path:str = "hangman\\assets\\words.csv") -> dict[str, str]:
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), path)
    words = {}
    try:
        with open(path) as csv:
            csv_data = reader(csv)
            for row in csv_data:
                words[row[0]] = row[1]
    except Exception as e:
        print(f"Error : {e}");
    return words


def get_word_dict() -> dict[str, str]:
    words = __get_words_from_csv()
    unique_words = {}
    unique_word_set = {i for i in words.keys()}
    unique_words = {i : words[i] for i in unique_word_set}
    return unique_words
