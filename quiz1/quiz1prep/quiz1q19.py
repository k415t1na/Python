#Write a program to ask the user to enter a number and then check and display whether the number is:Divisible by 2Divisible by 3Divisible by both 2 and 3.

a=float(input("enter one number: "))

if a%2==0 and a%3==0:
    print("the number is divided by 2 and 3!!")

elif a%3==0:
    print("the number is divided bu 3!")

elif a%2==0:
    print("the number is divided by 2!")

else:
    print("the number is not divisible by 2 or 3")