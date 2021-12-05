#Create a function that can have a variable number of parameters and returns the sum of those parameters.
#E.g. magic(1, 3, 10) should return 14 , magic(10, 20, 5, 40) should return 75.

def magic(*args):
	sum = 0
	for num in args:
		sum += num

	return sum


print(magic(1, 3, 10))
print(magic(10, 20, 5, 40))