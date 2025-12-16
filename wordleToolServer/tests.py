from constants import WORDLE_WORDS_PATH
from wordle_solve import best_first_guesses, letter_count, load_words, possible_words

CASES = []


def load_words_test() -> dict:
    '''
    '''
    print('Loading word list..')
    word_list: list[str] = load_words(WORDLE_WORDS_PATH)
    print('Loaded words.')

    if not word_list:
        raise Exception('No words loaded')
    return word_list


def letter_count_test(word_list: list[str]) -> dict:
    '''
    '''
    print('Counting letters from the word list...')
    letter_counts: dict = letter_count(word_list)

    if not letter_counts:
        raise Exception('No letters counted')

    h_key = max(letter_counts, key=letter_counts.get)
    h_val = letter_counts[h_key]
    l_key = min(letter_counts, key=letter_counts.get)
    l_val = letter_counts[l_key]

    print(f'The most used letter in the Wordle dictionary is {h_key} with {h_val} appearances.')
    print(f'The least used letter in the Wordle dictionary is {l_key} with {l_val} appearances.')

    return


def first_guesses_test(word_list: list[str], vowel_count: int) -> dict:
    '''
    '''
    print(f'Finding best first guesses ({vowel_count} or more vowels) from word list:')
    best_guesses: list[str] = best_first_guesses(word_list, vowel_count)
    print(f'There are {len(best_guesses)} words with {vowel_count} or more vowels in the Wordle dictionary.')

    if not best_guesses:
        raise Exception('')
    return


def valid_guesses_test(word_list: list[str]) -> dict:
    '''
    '''
    known_letters = ['a', '_', '_', '_', 'o']
    unknown_letters = [[], [], ['e'], ['i', 'm'], []]
    known_letters = ['a', '_', '_', '_', 'o'],
    available_letters = ['q', 'w', 'e', 'r', 'y', 'u', 'i', 'o', 'f', 'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    print('Finding possible guesses for test cases ...')
    valid_guesses: list[str] = possible_words(known_letters, unknown_letters, available_letters, word_list)
    print(f'There are {len(valid_guesses)} possible guesses given the current game state.')

    if not valid_guesses:
        pass
    return


def main():
    word_list = load_words_test()
    letter_count_test(word_list)
    first_guesses_test(word_list, vowel_count=3)
    first_guesses_test(word_list, vowel_count=4)
    valid_guesses_test(word_list)


if __name__ == "__main__":
    main()
