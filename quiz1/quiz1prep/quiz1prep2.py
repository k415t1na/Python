#Create a python program that asks the user for one real number and then displays the number with 2 symbols after the decimal point, on 20 places, assigned in the center.

val= float(input("enter one number: "))


print(f"{val:^20.2f}")
