#Create a python program that asks the user for couple of numbers x and y and print the even numbers in the range [x, y].


a,b = int(input('first: ')), int(input('second: '))

for i in range(a,b,1):
	if not i%2:
		print(i)