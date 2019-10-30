Marmight is a cheater program for the board game [Letter Jam](https://boardgamegeek.com/boardgame/275467/letter-jam).

# Setup

1. Download a newline-delimited English wordlist, and save it in the root directory of this repo as `dictionary.txt`. A suggested wordlist is [here](https://github.com/dwyl/english-words/blob/master/words.txt).

# Usage

1. To guess a letter, from the root directory of the repo run `python src/app.py`.
2. Type in a clue and hit enter. This clue will be a string of the form `l*tt*?`, where `*` represents the wildcard, and `?` represents your letter that you are trying to guess.
3. Repeat step 2. until you get an unambiguous answer letter.
