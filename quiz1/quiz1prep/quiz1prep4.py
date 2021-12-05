#Create a python program that asks the user for string and then prints only the lowercase letters in the string.
string = input('String: ')

for i in string:
	if i.islower():
		print(i)