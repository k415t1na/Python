#Write a program to ask the user for a number, checks whether the number is of type int, and calculates the square root of the number if it is, otherwise checks whether it is a float and multiply it with pi if it is a float.

import math

number = eval(input('Number: '))

if type(number) == int:
	result = math.sqrt(number)
	print('Square root: ', result)

if type(number) == float:
	result = math.pi * number
	print('Multiply with pi: ', result)