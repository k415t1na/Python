#Write a program to ask the user for an integer and checks whether the number is a prime number. If the number is a prime number print "Prime" and "Not prime" otherwise.

number = int(input('Enter number: '))


not_prime = False

if number > 1:
    for it in range(2, number):
        if (number % it) == 0:
            not_prime = True
            break

if not_prime:
    print('Not a prime number')
else:
    print('Prime number')