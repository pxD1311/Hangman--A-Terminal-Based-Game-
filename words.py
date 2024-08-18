from csv import reader

def get_words_from_csv(path:str = "assets\\words.csv") -> dict[str, str]:
    words = {}
    with open(path) as csv:
        csv_data = reader(csv)
        for row in csv_data:
            words[row[0]] = row[1]
    return words


def get_unique_words(words : dict[str, str]) -> dict[str, str]:
    unique_words = {}
    unique_word_set = {i for i in words.keys()}
    unique_words = {i : words[i] for i in unique_word_set}
    return unique_words