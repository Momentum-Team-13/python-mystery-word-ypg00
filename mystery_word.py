import random

def decide_to_play():
    print('#' * 80)
    print(f'Would you like to play Mystery Word, Y/N?')
    decision_to_play = input()

    if decision_to_play == 'y' or decision_to_play == 'Y':
        play_game()
    elif decision_to_play == 'n' or decision_to_play == 'N':
        print('Well, okay then...')
        print('#' * 80)
    else:
        decide_to_play()

def play_game():
    answer_str = generate_word_for_game()
    answer_list = list(answer_str)
    # print(f'answer_list: {answer_list}')
    
    print_game_instructions(answer_str)

    guesses = []
    turns_remaining = 8

    while len(guesses) < 8:
        guess_character(guesses)
        guesses_str = ' '.join(guesses)
        print(f'Guesses: {guesses_str}')
        turns_remaining -= 1
        print(f'Turns remaining: {turns_remaining}\n')
        #check guesses list against answer
        display_list = [(char.replace(char, "_")) if char not in guesses else char for char in answer_list]
        display_str = ' '.join(display_list)
        print(f'Mystery Word: {display_str}')
    

def print_game_instructions(answer_str):
    print('#' * 80)
    print('Instructions:')
    print('1. You will have 8 turns at guessing characters for the answer.')
    print('2. You can try to guess the mystery word at the end of every turn.\n')
    print(f'Answer: {str(answer_str)}')
    print(f'Mystery Word length: {len(answer_str)} characters')
    print('Mystery Word: ' + ('_ ' * len(answer_str)))
    print('#' * 80)
    # print('\n')

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

def guess_character(guesses):
    guess = input('Guess a letter: ')
    if validate_guess(guess) == False:
        guess_character(guesses)
    else: 
        guess = guess.upper()
        return guesses.append(guess)

def validate_guess(guess):
    if len(guess) != 1:
        print('\nGuess a single letter at a time.')
        return False
    elif guess.isalpha() == False:
        print('\nYour guess must be a letter.')
        return False

if __name__ == "__main__":
    decide_to_play()