''' This program is designed to help find possible word guesses for a Wordle game.
'''


def best_first_guesses(words: list[str], vowel_limit: int = 3) -> list[str]:
    ''' Searches word list for words that could be considered 'good' first guesses.
    '''
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    best_guesses: list[str] = []

    for word in words:
        unique_vowels: list[str] = []
        unique_consonants: list[str] = []

        i = 0
        while i < len(word):
            letter = word[i]
            if letter in vowels and letter not in unique_vowels:
                unique_vowels.append(letter)
            elif letter not in unique_consonants:
                unique_consonants.append(letter)
            i += 1
        '''
        if len(unique_vowels) + len(unique_consonants) >= 4 and len(unique_vowels) >= 3:
            best_guesses.append(word)
        '''
        if len(unique_vowels) + len(unique_consonants) >= 4 and len(unique_vowels) >= vowel_limit:
            best_guesses.append(word)

    return best_guesses


def possible_words(known_letters: list[str],
                   unknown_letters: list[list[str]],
                   eliminated: list[str],
                   words: list[str]) -> list[str]:
    '''Finds all possible words that match the known letters and available letters.'''
    possible_words: list[str] = []

    for word in words:
        is_possible = True
        i = 0
        while i < len(word) and is_possible:
            letter = word[i]
            # check if the letter and location match the known letters' positioning.
            if known_letters[i] != '_' and known_letters[i] != letter:
                is_possible = False
            # check to see if the letter is in a position that we know is not correct.
            if letter in unknown_letters[i]:
                is_possible = False
            # check to see if the letter is outside of the available letters.
            if letter in eliminated:
                is_possible = False
            i += 1
        if is_possible:
            possible_words.append(word)
    return possible_words


def load_words(file_path: str) -> list[str]:
    words: list[str] = []
    try:
        with open(file_path, "r") as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    if words:
        print(f"Loaded {len(words)} words from the file.")
    else:
        print("No words were loaded from the file.")

    return words


def letter_count(word_list: list[str]) -> dict:
    '''
    reads letter counts from word list
    '''
    counts: dict = {}

    for word in word_list:
        for letter in word:
            if counts.get(letter, None):
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts
