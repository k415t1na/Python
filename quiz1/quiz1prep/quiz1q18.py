#Write a program that calculates the weekly salary of an employee, given the number of hours worked and hourly rate.Weekly hours exceeding 40 are paid at a rate of one time and a half.

hrs=float(input("enter the number of hours: "))
hr_rate= float(input("enter the hourly rate: "))

if hrs<=40:
    print("the weekly salary is: ", hrs*hr_rate)

else:
    overtime_hrs=hrs-40
    overtime_payment=overtime_hrs*hr_rate*1.5
    normal_payment=40*hr_rate
    print("the weekly salary is: ", normal_payment+overtime_payment)