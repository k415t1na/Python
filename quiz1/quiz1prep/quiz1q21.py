#Write a python program to ask the user to enter three numbers - lower, upper bound and step and print the current number in the for loop. Include else clause to print the count control variable.

upper = int(input('Upper bound: '))
lower = int(input('Lower bound: '))
step = int(input('Step: '))

index = 1
for i in range(lower, upper + 1, step):
    print(f'number {index}: {i}')
    index += 1



