#Write a python program that should create a while True loop that will randomly generates a number ([0-9]) and will print it. The while loop should break once the randomly generated number is 0.


import random

while True:
	next = random.randint(0, 9)
	if next==0:
		print('Random was 0')
		break

	print(next)