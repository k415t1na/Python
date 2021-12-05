#Create a program to read a text file called input.txt and create an output.txt file to copy the contents of the input.txt but without the uppercase letters.


def main():
	
	with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
		content = input.read()
		

		for line in content:
			new_line = ''
			for char in line:
				if not char.isupper():
					new_line+=char 
			output.write(new_line)


if __name__ == "__main__":
	main()