#Create a python program that asks for three numbers and calculates the formula below and displays the result.

a,b,c = int(input('a: ')), int(input('b: ')), int(input('c: '))

solution = ((a+b)/(2*c)) + (c*c)


print(f'result {solution}')