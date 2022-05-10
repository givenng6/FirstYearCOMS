def read_dictionary():
    """
    Read in the dictionary from standard input and return it as a list
    :return: the dictionary
    """
    words = []
    word = input().upper()

    while(word != '###'):
        words.append(word)
        word = input().upper()
        
    return words



def compute_response(target, guess):
    """
    Given the hidden word and a guess, return a string representing whether the letters are correct (and in the correct
    place)
    :param target: the hidden word
    :param guess: the guess the user has just made
    :return: a string indicating how correct they are (see Task 6)
    """
    hidden = target
    word = ''
    for i in range(len(target)):
        if guess[i] in target:
            word = word + guess[i].upper()
        else:
            word = word + '.'
        
    for i in range(len(word)):
        val = word[i]
        if val != '.':
            c_hidden = 0
            c_word = 0
            for c in range(len(hidden)):
                if hidden[c] == val:
                    c_hidden = c_hidden + 1
                if word[c] == val:
                    c_word = c_word + 1
            if c_word > c_hidden:
                index = []
                for k in range(len(hidden)):
                    if word[k] == val:
                        if hidden[k] != val:
                            index.append(k)
                if len(index) > 1:
                    for j in range(len(index)-1, 0, -1):
                        if c_word > c_hidden:
                            temp = word 
                            word = ''
                            for l in range(len(temp)):
                                if l == index[j]:
                                    c_word = c_word - 1
                                    word = word + '.'
                                else:
                                    word = word + temp[l]
                else:
                    for j in range(len(index)):
                        if c_word > c_hidden:
                            temp = word 
                            word = ''
                            for l in range(len(temp)):
                                if l == index[j]:
                                    c_word = c_word - 1
                                    word = word + '.'
                                else:
                                    word = word + temp[l]
    output = ''
    for i in range(len(hidden)):
        if word[i] == hidden[i]:
            output = output + word[i]
        else:
            output = output + word[i].lower()
            
    return output

                
def is_valid(guess, dictionary):
    """
    Given a guess by the user and the dictionary, determine whether the guess is a valid one to make (see Task 2)
    :param guess: the user's guess
    :param dictionary: a list of all words in the dictionary
    :return: True if the guess is valid; otherwise, return False
    """
    if len(guess) == 5:
        if guess in dictionary:
            return True
        else:
            return False
    else:
        return False
    
    
    

"""
DO NOT MODIFY ANY CODE BELOW THIS LINE
"""

import random

dictionary = read_dictionary()

rng = random.Random(0)

while True:

    choice = input("Play a game? (Y/N): ")
    if choice == 'N':
        break

    target = dictionary[rng.randint(0, len(dictionary) - 1)]
    turns = 0
    MAX_TURNS = 6
    while True:
        if turns == MAX_TURNS:
            print("Game over! :(")
            print('The word was: {}'.format(target))
            break
        else:
            guess = input()
            while not is_valid(guess, dictionary):
                print('{} is not a valid word!'.format(guess))
                guess = input()

            print("You guessed: {}".format(guess))
            response = compute_response(target, guess)
            print('Response: {}'.format(response))
            if response == guess:
                # we won!
                print("You win! :)")
                break
        turns += 1

