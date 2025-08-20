''' This program is designed to help find possible word guesses for a Wordle game.
'''


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
            # check if the letter and location mathch the known letters' positioning.
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


def main():
    ''' This file can run as main() for testing purposes, but recommend to use as a module.
    '''
    words: list[str] = load_words("valid-wordle-words.txt")
    print(possible_words(
        known_letters=['a', '_', '_', '_', 'o'],
        unknown_letters=[[], [], ['e'], ['i', 'm'], []],
        available_letters=['q', 'w', 'e', 'r', 'y', 'u', 'i', 'o', 'f', 'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm'],
        words=words
    ))


if __name__ == "__main__":
    main()
