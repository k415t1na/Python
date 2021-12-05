#Write a python program that asks the user for a year. Checks whether the number is valid if not –prints an error, if yes checks whether it is a leap year and shows the result.

year=input("enter a year: ")

if type(year) == int:
    while True:
        if(year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            print(year, "is a leap year")
            break
    
        else:
            print("this is not a leap year, enter anohter one.")
            year=int(input("enter a year: "))

else:
    print('The variable is not a number')


