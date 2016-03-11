# Assignment 2: Introduction to Python
# Script 1

# Jaime Hoffman
# California State University, Northridge
#________________________________________

# import datetime module & get current year
import datetime

# function to calculate user's age
def calculateAge(name, DOB):

	# calculate the users age
	userAge = currentYear - DOB

	# return string with name and age
	return "{0} is {1} years old.".format(name, userAge)

currentYear = datetime.datetime.now().year

# ask user for their information
userName = raw_input("Please enter your name: ")
userDOB = int(raw_input("Please enter the year you were born: "))

print calculateAge(userName, userDOB)