import random
from words import words
import string


# RANDOM WORD GETS CHOSEN
def get_valid_word(words):
    random_word = random.choice(words)
    if '-' in random_word:
        random_word = random.choice(words)
    return random_word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # LETTERS IN WORD
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # USED LETTERS

    lives = 5

    # USER INPUT
    while len(word_letters) > 0 and lives > 0:
        # LETTERS USED
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # WHAT CURRENT WORD IS - EX: W-ORD
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Enter a letter: ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1
                print('\nYour letter,', user_letter, 'is not in the word.')

    # GAME OVER
    if lives == 0:
        print("\nYou have lost. The word was ", word)

    else:
        print("\nThe word ", word, " was correct!")



hangman()
