'''
Guess the Word Game (Answer with annotations)

By: Monique Cheng
'''

# import random library
from random import randint

# initialize word list
words = ["apple", "cow", "python", "telephone", "rocket", "orange", "google"]

# select the random word through the randint() function
word = words[randint(0, len(words) - 1)]
# print the length of the word using len()
print("This word is " + str(len(word)) + " letters long")
# prompt the user to input their guess
guess = input("Enter your guess: ")
# an infinite loop while the user guesses the word
while (True):
    # if the guess is correct, use 'break' to exit this while loop
    if (guess.lower() == word):
        print("You guessed it! Good job!")
        break
    # if the guess is incorrect, let the user know and prompt them to enter another guess
    else:
        print("Sorry that was wrong! Try again!")
    guess = input("Enter your guess: ")
    
# 'game over' message!
print("Thank you for playing!")
