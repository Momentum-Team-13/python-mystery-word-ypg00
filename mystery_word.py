import random

def play_game():
    guesses_list = []
    turns_remaining = 8

    decide_to_play()
    ANSWER_STR = generate_word_for_game()
    ANSWER_LIST = list(ANSWER_STR)
    print_game_instructions(ANSWER_STR, turns_remaining)

    while turns_remaining > 0:
        guess = guess_letter(guesses_list)
        guesses_list.append(guess)
        # Casting the list of guesses as a string for cleaner terminal presentation
        guesses_str = str(' '.join(guesses_list))

        # Check guesses_list against ANSWER_LIST for matches
        display_list = [(char.replace(char, "_")) if char not in guesses_list else char for char in ANSWER_LIST]
        # Casting the list as a string for cleaner terminal presentation
        display_str = ' '.join(display_list)

        # Check if solved
        if display_list == ANSWER_LIST:
            print('\nYou solved it!\n')
            print(f'The Mystery Word was {ANSWER_STR}.\n')
            break
        
        # Lose a turn if guess is incorrect
        if guess not in ANSWER_LIST:
            turns_remaining -= 1
        
        # Print status report
        print('\n' + '#' * 80 + '\n')
        print(f'Turns remaining: {turns_remaining}')
        print(f'Guesses: {guesses_str}\n')
        print(f'Mystery Word: {display_str}\n')
    
def decide_to_play():
    print('\n' + ('#' * 80) + '\n')
    decision_to_play = input('Would you like to play Mystery Word, Y/N? ').upper()

    if decision_to_play == 'Y':
        pass
    elif decision_to_play == 'N':
        print('\nWell, okay then...')
        print('\n' + ('#' * 80) + '\n')
    else:
        decide_to_play()

def print_game_instructions(ANSWER_STR, turns_remaining):
    print('\n' + ('#' * 80) + '\n')
    print('Instructions:\n')
    print(f'1. You are allowed {turns_remaining} incorrect guesses before losing the game.')
    print('2. You can try to guess the Mystery Word at the end of every turn.')
    print(f'3. The Mystery Word is {len(ANSWER_STR)} characters long.')
    print('\n' + ('#' * 80) + '\n')
    print('Mystery Word: ' + ('_ ' * len(ANSWER_STR)) + '\n')
    # print(f'Answer: {str(ANSWER_STR)}')

def generate_word_for_game():
    # Open file as read
    file = 'words.txt'
    with open(file) as open_file:
        read_file = open_file.read()

    # Turn the file into a list of strings
    available_words = str.split(read_file)

    # Create an random index number
    index = random.randint(0, (len(available_words) - 1))

    # Select a word for the game using the random index number
    word_str = available_words[index]

    # Uppercase the string
    word_str_upper = word_str.upper()
    
    # Return word for the game
    return word_str_upper

def guess_letter(guesses_list):
    guess = input('Guess a letter: ').upper()

    # Validating the guess
    if len(guess) != 1:
        print('\nGuess a single letter at a time.\n')
        return guess_letter(guesses_list)
    elif guess.isalpha() == False:
        print('\nYour guess must be a letter.\n')
        return guess_letter(guesses_list)
    elif guess in guesses_list:
        print(f'\nYou\'ve already guessed {guess}, try again.' + '\n')
        return guess_letter(guesses_list)
    else:
        return guess

def print_end_game_msg():
    pass

if __name__ == "__main__":
    play_game()