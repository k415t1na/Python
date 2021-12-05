#Write a program to ask the user for a number – validate whether the number is in the range [1, 20] and displays a message stating whether the number is in the range or not.

a=float(input("enter one number: "))

if a>=1 and a<=20:
    print("the number is in the interval [1:20]")

else:
    print("the number is not in the range [1:20]. ")