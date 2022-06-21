import random

def decide_to_play():
    print('#' * 80)
    print('Would you like to play Mystery Word, Y/N?')
    deciding_to_play = input()

    if deciding_to_play == 'y' or deciding_to_play == 'Y':
        print('#' * 80)
        generate_word_for_game()
    elif deciding_to_play == 'n' or deciding_to_play == 'N':
        print('Well, okay then...')
        print('#' * 80)
    else:
        play_decision()

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
    play_game(answer)

def play_game(answer):
    # Print instructions here

    print(f'Answer: {answer}')
    print('_' * len(answer))



if __name__ == "__main__":
    decide_to_play()