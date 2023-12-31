#milestone_5.py

import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Loop through each letter in the word
            for idx, letter in enumerate(self.word):
                # Check if the letter is equal to the guess
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1

        else:
            # If the guess is not in the word
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess.lower())
                self.check_guess(guess)
                break  # Exit the loop once valid input is received and checked


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_for_input()
        print(' '.join(game.word_guessed))  # To show the progress of guessed word
        
        if game.num_lives == 0:
            print("You lost!")
            break

        if game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break

# Call the play_game function
word_list = ["apple", "banana", "blackberry", "avocado", "blueberry"]
play_game(word_list)
