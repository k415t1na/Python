#Write a python program, which will ask the user to enter one number and then will display the result of applying three functions (whatever you like) from the math module.

import math

number = float(input('Enter number: '))

# Round up
print(f'Round up: {math.ceil(number)}')

# Find consine of number
print(f'Cosine: {math.cos(number)}')

# Find sqrt of number
print(f'Square root: {math.sqr}')
