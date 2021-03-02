'''
Guess the Word Game (Answer with annotations)

By: Monique Cheng
'''

# import random library
from random import randint

# initialize word list
words = ["apple", "cow", "python", "telephone", "rocket", "orange", "google"]

# use an infinite while loop, we will use 'break' to get out of this loop later
while (True):
    # select the random word through the randint() function
    word = words[randint(0, len(words) - 1)]
    # print the length of the word using len()
    print("This word is " + str(len(word)) + " letters long")
    # prompt the user to input their guess
    guess = input("Enter your guess: ")
    # another infinite loop while the user guesses the word
    while (True):
        # if the guess is correct, use 'break' to exit this while loop
        if (guess.lower() == word):
            break
        # if the guess is incorrect, let the user know and prompt them to enter another guess
        else:
            print("Sorry that was wrong! Try again!")
        guess = input("Enter your guess: ")
    # print good job to let the user know they have answered it correctly outside the while loop
    # the user will only see this once the infinite guessing loop is exited
    print("You guessed it! Good job!")
    # set the variable tryAgain
    tryAgain = ""
    # while the user doesn't input 'yes' or 'no' as a response...
    while (tryAgain != "yes" and tryAgain != "no"):
        # prompt the user to input a response
        tryAgain = input("Would you like to try again? (yes or no)")
    # if the user inputs 'no', exit the while loop to end the game
    if (tryAgain == "no"):
        break
# 'game over' message!
print("Thank you for playing!")
