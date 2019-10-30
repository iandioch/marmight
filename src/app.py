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



def main():
    # TODO(iandioch): Allow dictionary file to be configured.
    DICT_FILE = './dictionary.txt'
    with open(DICT_FILE, 'r') as f:
        dictionary = [w.strip().lower() for w in f]

    # TODO(iandioch): Make word length configurable.
    WORD_LENGTH = 5


    # TODO(iandioch): Limit this set to only the words that come up in the game.
    poss_letter_set = set('abcdefghijklmnopqrstuvwxyz')
    clues = []
    while True:
        clue = input().strip().lower()
        if clue == 'exit':
            break
        clues.append(clue)
        poss_letter_set = get_possible_letters(dictionary, [clue], poss_letter_set)
        print(len(poss_letter_set), 'possible letter(s):', ', '.join(sorted(poss_letter_set)))
        if len(poss_letter_set) == 1:
            print('Answer:', next(iter(poss_letter_set)))
            break
        if len(poss_letter_set) == 0:
            print('No known letters. Maybe a clue was a non-dictionary word?')
            break

if __name__ == '__main__':
    main()
