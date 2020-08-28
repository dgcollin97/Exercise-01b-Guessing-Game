import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
hundred = 300
guess = input("Guess a hundred from 100 to 900: ")
guess = int(guess)
if guess == hundred:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The hundred was " + str(hundred))
