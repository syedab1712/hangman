import random

#milestone_2.py

# Step 1: Create a list containing the names of your 5 favorite fruits.
fruits = ["apple", "banana", "blackberry", "mango", "blueberry"]

# Step 2: Assign this list to a variable called word_list.
word_list = fruits

# Step 3: Use the random.choice method and pass the word_list variable into the choice method.

# Step 4: Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Step 5: Using the input function, ask the user to enter a single letter.
# user_input = input("Please enter a single letter: ")

# Step 6: Assign the input to a variable called guess.
# guess = user_input


#milestone_2.py
'''
# Step 7: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")

print("You entered:", guess)

'''



#Milestone_3.py

'''

# Step 1: Create a while loop and set the condition to True.
while True:
    
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Please guess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            # Step 3: Create an else block.
            print(f"Sorry, {guess} is not in the word. Try again.")

        
    
    else:
        # Step 5: If the guess does not pass the checks, then print a message.
        print("Invalid letter. Please, enter a single alphabetical character.")
        
'''

'''
# Define the check_guess function
def check_guess(guess):
    # Convert the guess to lowercase
    guess = guess.lower()
    
    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
    

def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")
        
        # Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess):  # This will also print the appropriate message
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()

'''

