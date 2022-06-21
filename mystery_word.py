import random

def decide_to_play():
    print('#' * 80)
    print('Would you like to play Mystery Word, Y/N?')
    deciding_to_play = input()

    if deciding_to_play == 'y' or deciding_to_play == 'Y':
        play_game()
    elif deciding_to_play == 'n' or deciding_to_play == 'N':
        print('Well, okay then...')
        print('#' * 80)
    else:
        play_decision()

def play_game():
    print_game_instructions()
    answer = generate_word_for_game()

    print(f'Answer: {answer}')
    print('_' * len(answer))

    guesses = []
    while len(guesses) < 8:
        guesses.append(guess_character())
    
    print(f'guesses: {guesses}')
    
    #check guesses list against answer
    new_list = [char for char in guesses if char in answer]
    print(new_list)


    #render new result
    #


def print_game_instructions():
    print('#' * 80)
    print('Instructions:')
    print('1. You will have 8 turns, or guesses, at characters for the answer.')
    print('2. You can guess the word at the end of every turn.')
    print('#' * 80)

def generate_word_for_game():
    # Open words.txt as read
    file = 'words.txt'
    with open(file) as open_file:
        read_file = open_file.read()

    # Turn the file into a list of strings
    word_list = str.split(read_file)

    # Select and return a random word from the list
    index = random.randint(0, (len(word_list) - 1))
    answer = word_list[index]
    return answer

def guess_character():
    guess = input('Guess a letter:\n')
    return guess

if __name__ == "__main__":
    decide_to_play()