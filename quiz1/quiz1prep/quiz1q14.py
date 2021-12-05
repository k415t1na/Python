#Write a python program, which will ask the user to enter two numbers and then will format them – the first one as integer, then second one as float with 6 digits after the floating point.


first = int(input('First number: '))
second = float(input('Second number: '))


print(first)
print(f'{second:.6f}')
