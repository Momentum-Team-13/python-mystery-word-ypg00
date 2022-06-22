import random

def decide_to_play():
    print('\n' + ('#' * 80) + '\n')
    decision_to_play = input('Would you like to play Mystery Word, Y/N? ').upper()

    if decision_to_play == 'Y':
        play_game()
    elif decision_to_play == 'N':
        print('\nWell, okay then...')
        print('\n' + ('#' * 80) + '\n')
    else:
        decide_to_play()

def play_game():
    answer_str = generate_word_for_game()
    answer_list = list(answer_str)
    guesses_list = []
    turns_remaining = 8
    
    print_game_instructions(answer_str)

    while turns_remaining > 0:
        guess = guess_letter(guesses_list)
        guesses_list.append(guess)
        guesses_str = str(' '.join(guesses_list))

        # Lose a turn if guess is incorrect
        if guess not in answer_list:
            turns_remaining -= 1

        # Check guesses_list against answer_list to create what to display
        display_list = [(char.replace(char, "_")) if char not in guesses_list else char for char in answer_list]
        display_str = ' '.join(display_list)

        # Check if solved
        if display_list == answer_list:
            print('\nYou solved it!')
            print(f'The Mystery Word was {answer_str}.')
            break
        
        # Print status report
        print(f'\nTurns remaining: {turns_remaining}')
        print(f'Guesses: {guesses_str}')
        print(f'Mystery Word: {display_str}\n')

        # print(f'guesses_list: {guesses_list}')
        # print(f'answer_list: {answer_list}')
        # print(f'display_list: {display_list}\n')
    
def print_game_instructions(answer_str):
    print('\n' + ('#' * 80) + '\n')
    print('Instructions:')
    print('1. You will have 8 turns at guessing characters for the Mystery Word.')
    print('2. You can try to guess the Mystery Word at the end of every turn.\n')
    print(f'Answer: {str(answer_str)}')
    print(f'Mystery Word length: {len(answer_str)} characters')
    print('Mystery Word: ' + ('_ ' * len(answer_str)))
    print('\n' + ('#' * 80) + '\n')

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
    decide_to_play()