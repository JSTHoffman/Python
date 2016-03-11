# Assignment 2: Introduction to Python
# Script 2

# Jaime Hoffman
# California State University, Northridge
#________________________________________

# import random number module
import random

# function to check user's guess
def checkGuess(guess):

	if userGuess > randomNum:
		print "Too high! Guess again."

	elif userGuess < randomNum:
		print "Too low! Guess again."
		
	else:
		print "Perfect guess!"

# generate random number between 1 and 100
# (both endpoints are included)
randomNum = random.randint(1, 100)

# variable to store user's guess
userGuess = 0

#ask user to guess a number between 1 & 100
print "Please guess a number between 1 & 100."

while userGuess != randomNum:

	# get the user's guess
	userGuess = int(raw_input("--> "))

	# compare guess to random number
	checkGuess(userGuess)