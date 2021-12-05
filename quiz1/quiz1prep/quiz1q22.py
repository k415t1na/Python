#Write a python program to ask the user to enter an integer. Check whether the number is an integer, if not -  print some error message and ask again for a number. Loop the input statement till a valid number is entered. If the number is an integer then check whether it is even or odd and print the result.


def is_integer(i):
    try:
        new_i = int(i)
        return isinstance(new_i, int)
    except Exception as err:
        return False

n = None

while not is_integer(n):
    n = input('Number: ')
    
    if is_integer(n):
        if int(n) % 2==0:
            print(f'{n} is Even')
        else:
            print(f'{n} is Odd')
        break
    
    else:
        print(f'{n} is not integer')