# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from constants import REACT_APP_URL, WORDLE_WORDS_PATH
import wordle_solve

WORDS: list[str] = wordle_solve.load_words(WORDLE_WORDS_PATH)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[REACT_APP_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/words")
def get_words():
    return {"words": WORDS}


@app.get("/filter_words")
def filter_words(known: str = Query(...), nonmatching: str = Query(...), eliminated: str = Query(...)) -> dict:
    ''' Filters words based on previous Wordle guesses.

        Args:
            known (list[str]): List of known letters in the word, with '_' for unknown positions.
            nonmatching (list[str]): List of letters that are in the word, but not in the correct position.
            eliminated (str): Letters that are known to be eliminated from the word.
    '''
    # FIXME: need to update this code because the request will have .join()ed the data.
    # we should use a method to parse the query before passing to this function
    print(f'known: {known}')
    print(f'nonmatching: {nonmatching}')
    print(f'eliminated: {eliminated}')

    guesses: list[str] = wordle_solve.possible_words(known_letters=known.split(','),
                                                     unknown_letters=nonmatching.split(','),
                                                     eliminated=eliminated,
                                                     words=WORDS)
    print(f'words calculated: {guesses}')
    return {"words": guesses}
