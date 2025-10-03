# Write a program that will:Ask the user to input a string
#from random import random

#Select a random character in the string - call this the ‘tumor’
#Tell the user what the tumor is, and remove all instances of the tumor in the string
#Print out the resulting word after the character has been removed
#Note: Make sure you don’t select an index outside the string’s bounds

#As a hint, recall what we learned from class 2 about generating random integers
#how can you use this to find a random index in a string?


import random

str = str(input("Please enter a string: "))
tumour_ptr = random.randint(0, len(str)-1)
print(f"The the tumour is {str[tumour_ptr]}")
str = str.replace(str[tumour_ptr], "")
print(f"The resulting word is: {str}")

