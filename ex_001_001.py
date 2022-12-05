## QUESTION ##
'''
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

## SOLUTION ###

# Declare formatting variables
nl0 = "\n"
nl1 = "\n\t"
nl2 = "\n\t\t"

# Declare lines
line1 = "Twinkle, twinkle, little star,"
line2 = "How I wonder what you are!"
line3 = "Up above the world so high,"
line4 = "Like a diamond in the sky."
line5 = "How I wonder what you are"

# Print
print(line1, nl1, line2, nl2, line3, nl2, line4, nl0, line1, nl1, line5, sep="")