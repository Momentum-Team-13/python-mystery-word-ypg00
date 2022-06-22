import random

def decide_to_play():
    print('\n' + ('#' * 80) + '\n')
    # print(f'Would you like to play Mystery Word, Y/N?')
    decision_to_play = input('Would you like to play Mystery Word, Y/N? ')

    if decision_to_play == 'y' or decision_to_play == 'Y':
        play_game()
    elif decision_to_play == 'n' or decision_to_play == 'N':
        print('Well, okay then...')
        print('#' * 80)
        STOP
    else:
        decide_to_play()

def play_game():
    answer_str = generate_word_for_game()
    answer_list = list(answer_str)
    
    print_game_instructions(answer_str)

    guesses_list = []
    turns_remaining = 8

    for turn in range(turns_remaining):
        guess_character(guesses_list)
        guesses_str = ' '.join(guesses_list)
        turns_remaining -= 1

        # Check guesses_list list against answer
        display_list = [(char.replace(char, "_")) if char not in guesses_list else char for char in answer_list]
        display_str = ' '.join(display_list)

        print(f'\nTurns remaining: {turns_remaining}')
        print(f'Guesses: {guesses_str}')
        print(f'Mystery Word: {display_str}\n')
    
    print_end_game_msg()
    
def print_game_instructions(answer_str):
    print('\n' + ('#' * 80))
    print('\nInstructions:')
    print('1. You will have 8 turns at guessing characters for the Mystery Word.')
    print('2. You can try to guess the Mystery Word at the end of every turn.\n')
    print(f'Answer: {str(answer_str)}')
    print(f'Mystery Word length: {len(answer_str)} characters')
    print('Mystery Word: ' + ('_ ' * len(answer_str)) + '\n')
    print(('#' * 80) + '\n')

def generate_word_for_game():
    # Open words.txt as read
    file = 'words.txt'
    with open(file) as open_file:
        read_file = open_file.read()
    # Turn the file into a list of strings
    list_of_available_words = str.split(read_file)
    # Create an random index number
    index = random.randint(0, (len(list_of_available_words) - 1))
    # Select a word for the game using the random index number
    word_for_game_as_str = list_of_available_words[index]
    # Uppercase the string
    upper_word_for_game_as_str = word_for_game_as_str.upper()
    # Return word, as a list, for the game
    return upper_word_for_game_as_str

def guess_character(guesses_list):
    guess = input('Guess a letter: ').upper()
    if validate_guess(guess, guesses_list) == False:
        guess_character(guesses_list)
    else: 
        return guesses_list.append(guess)

def validate_guess(guess, guesses_list):
    if len(guess) != 1:
        print('\nGuess a single letter at a time.')
        return False
    elif guess.isalpha() == False:
        print('\nYour guess must be a letter.')
        return False
    elif guess in guesses_list:
        print(f'You\'ve already guessed {guess}, try again.' + '\n')
        return False

if __name__ == "__main__":
    decide_to_play()