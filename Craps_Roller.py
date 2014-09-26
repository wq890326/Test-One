# Craps Roller
# Demonstrates random number generation
# Original Author: Michael Dawson
# Last Edited: Thorin Schmidt
# Date Edited: 9/26/2014

impart random

# generate random numbers 1 - 6
die1 = random.randint(1, 6) 
die2 = random.randrange(6)

total = 'die1' + 'die2'

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")
