#Write a python program, which will ask the user to enter two numbers and then will display the sum and division of the two numbers. Use float division and display the division with 3 digits after the decimal point.
first = float(input('First number: '))
second = float(input('Second number: '))

print(f'Sum = {round(first+second, 3)}')
print(f'Division = {(first/second):.3f}')
