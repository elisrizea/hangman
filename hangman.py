import random

# Save colors in constants to decorate the console output
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'
MAG = '\u001b[35m'


#  ************ Chose a random word from a tulip of 100 words **********
def chose_word():
    words = (
        'peaceful', 'pleasant', 'trucks', 'hammer', 'connect', 'immense', 'amused', 'ambitious',
        'toothbrush', 'force', 'robin', 'party', 'omniscient', 'internal', 'entertain',
        'camp', 'deceive', 'loud', 'muscle', 'protest', 'groomed', 'chubby', 'tomatoes',
        'various', 'flawless', 'panicky', 'unequal', 'gentle', 'succinct', 'physical',
        'demonic', 'nation', 'divide', 'messy', 'nervous', 'treat', 'broad', 'bike', 'jaded',
        'punishment', 'collar', 'helpful', 'adventurous', 'arrange', 'sidewalk', 'frantic',
        'overconfident', 'boring', 'evanescent', 'analyze', 'office', 'whistle', 'offend', 'woozy',
        'profit', 'thing', 'scandalous', 'false', 'forgetful', 'temporary', 'page', 'rake', 'lethal',
        'half', 'space', 'cheat', 'trousers', 'premium', 'field', 'perform', 'snakes', 'cowardly',
        'victorious', 'bouncy', 'sloppy', 'ambiguous', 'incandescent', 'sweltering', 'unsuitable',
        'mundane', 'request', 'possessive', 'rainstorm', 'attractive', 'prevent', 'stroke',
        'impartial', 'teeny', 'disarm', 'troubled', 'brawny', 'subsequent', 'hallowed', 'afraid',
        'fierce', 'notebook', 'snatch', 'synonymous', 'somber', 'condemned',
    )
    return words[int(round(random.random(), 2) * 100)]


# ********************** Play game ************************
def hangman(count):
    c = count
    indexes = []
    tryed_letter = []
    word = str(chose_word())
    _word = word
    print_word = ''
    for i in range(len(word)):
        print_word += '_'

    # Check if input letter is in initial word and not in guess word.
    # If true replace it with a "_" and replace a "_" with it in the guess word
    # and reset the Bed Choice counter to the initial value set by chosen game difficulty.
    # If false decrease the Bed Choice counter
    while True:
        print(f'Word : {print_word}')
        # Ignore case and spaces. Prevent user multiple character input (select just first char entered)
        letter = input('Please enter a letter:').strip().lower()
        if letter != '':
            letter=letter[0]
        tryed_letter.append(letter)
        print(f'Letter already tried :{tryed_letter}')
        print()
        if letter in word and letter not in print_word:
            count = c
            print(f'{GREEN}Good choice{END}')
            if letter in print_word:
                print(f'{RED}Bad choice. You already discover this letter{END}')
                count -= 1
                print(f'{RED}{count} more and you loose.{END}')
            else:
                while letter in _word:
                    index = _word.find(letter)
                    indexes.append(index)
                    _word = _word[:index] + '_' + _word[index + 1:]
                    print_word = print_word[:index] + letter + print_word[index + 1:]

        else:
            print(f'{RED}Bad choice.{END}')
            count -= 1
            print(f'{RED}{count} more and you loose.{END}')
        # Uncomment the next line to check the program functionality easy
        # print(word)

        # Game over.
        # Game Lost.
        if count <= 0:
            print()
            print(f'The word you had to guess was  {GREEN}{word.upper()}{END}')
            print(f'{RED}You lost. Better luck next time{END}')
            print('Goodbye!!!')
            exit()

        # Game over.
        # Game Win.
        if "_" not in print_word:
            print()
            print(f'{GREEN}CONGRATULATION You win!{END}')
            print('Goodbye!!!')
            exit()


# ********************** Main menu ************************
while True:
    print(f' {BLUE}********************** Main Menu **********************\n')
    # Ignore case and spaces. Prevent user multiple character input (select just first char entered)
    menu = input(f'''Please select the difficulty level:
                {MAG}e{BLUE}    - {MAG}E{BLUE}asy (6 wrong consecutive choices)
                {MAG}m{BLUE}    - {MAG}M{BLUE}edium (4 wrong consecutive choices)
                {MAG}h{BLUE}    - {MAG}H{BLUE}ard (2 wrong consecutive choices)      
                {MAG}q{BLUE}   -  To end program type {MAG}q{BLUE}uit.
{MAG}Enter your choice: {END}''').strip().lower()
    if menu !='':
        menu=menu[0]

    # Request input and call the necessary function
    if menu == 'e':
        print(f"""
{BLUE}================ Easy mode on =========================={END}""")
        # Easy mode
        hangman(6)
        break

    elif menu == 'm':
        print(f"""
{BLUE}================ Medium mode on =========================={END}""")
        # Easy Medium
        hangman(4)
        break

    elif menu == 'h':
        print(f"""
{BLUE}================ Hard mode on =========================={END}""")
        # Easy Hard
        hangman(2)
        break

    # Exit program
    elif menu == 'q':
        print('Goodbye!!!')
        exit()
    else:
        print(
            f'{RED}Please try again and type: '
            f'{GREEN}e{END} or {GREEN}m{END} or {GREEN}h{END} or {GREEN}q{END}')
        continue
