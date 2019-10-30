def get_possible_letters(dictionary, clues, poss_letter_set):
    print('Possible letters:', sorted(poss_letter_set))
    # TODO(iandioch): Support wildcards in clues.
    for clue in clues:
        poss_words = []
        poss_letters = set()
        for dic_word in dictionary:
            if len(clue) != len(dic_word):
                continue
            # length of word is == length of clue
            poss_for_this_clue = set()
            clue_matches = True
            poss_wildcards = set()
            for i in range(len(clue)):
                cl = clue[i]
                dwl = dic_word[i]
                if cl == '?':
                    # TODO(iandioch): Check for repeated ?s in the clue.
                    poss_for_this_clue.add(dwl)
                elif cl == '*':
                    poss_wildcards.add(dwl)
                elif cl != dwl:
                    clue_matches = False
                    break
            if clue_matches and len(poss_for_this_clue) == 1 and len(poss_wildcards) <= 1:
                poss_letters.add(next(iter(poss_for_this_clue)))
                poss_words.append(dic_word)
        print('Possible words for clue {}: {}'.format(clue, poss_words))
        poss_letter_set &= poss_letters
    return poss_letter_set

def solve_word(dictionary, letters):
    # A player can stop guessing at a letter even if there is ambiguity in what
    # it could be. For example, they might move onto the next letter if they
    # know their previous letter is either an A or a B, hoping to use the other
    # letters later to figure out what the earlier letter was. If they deduce
    # their other letters are I, N, R, and G, they can deduce that their word
    # was BRING, assuming that B and not A was the original letter.
    # This possible_letter_combinations list enumerates all the possible
    # combinations of letters the player knows. In the above scenario, it will
    # hold ['AINRG', 'BINRG']. This list of combinationrs can then be combined
    # with a wordlist to see which combinations are actually possible, knowing
    # that they create a word in the end.
    possible_letter_combinations = ['']
    for letterset in letters:
        new_combo = []
        for letter in letterset:
            for p in possible_letter_combinations:
                new_combo.append(p + letter)
        possible_letter_combinations = new_combo
    print(possible_letter_combinations)
    
    sorted_to_word = {''.join(sorted(w)):w for w in dictionary}
    possible_words = []

    for letters in possible_letter_combinations:
        sorted_letters = ''.join(sorted(letters))
        for sorted_word in sorted_to_word:
            if sorted_letters == sorted_word:
                possible_words.append(sorted_to_word[sorted_word])

    return possible_words



def main():
    # TODO(iandioch): Allow dictionary file to be configured.
    DICT_FILE = './dictionary.txt'
    with open(DICT_FILE, 'r') as f:
        dictionary = [w.strip().lower() for w in f]

    # TODO(iandioch): Make word length configurable.
    WORD_LENGTH = 5


    # TODO(iandioch): Limit this set to only the words that come up in the game.
    poss_letter_set = set('abcdefghijklmnopqrstuvwxyz')
    prev_letters = []
    while True:
        print('Insert "/exit", "/next", or "/solve", or input a clue.')
        user_input = input().strip().lower()
        if user_input == '/exit':
            print('\nBye!')
            break
        elif user_input == '/next':
            print('\nMoving onto next letter.')
            prev_letters.append(poss_letter_set)
            poss_letter_set = set('abcdefghijklmnopqrstuvwxyz')
            continue
        elif user_input == '/solve':
            print('\nSolving...')
            prev_letters.append(poss_letter_set)
            poss_words = solve_word(dictionary, prev_letters)
            print('Possible solution words:')
            print(', '.join(sorted(poss_words)))
            break
        poss_letter_set = get_possible_letters(dictionary, [user_input], poss_letter_set)
        print(len(poss_letter_set), 'possibilities for this letter:', ', '.join(sorted(poss_letter_set)))
        if len(poss_letter_set) == 0:
            print('No known letters. Maybe a clue was a non-dictionary word?')
            break

if __name__ == '__main__':
    main()
