#Write a program that reads an integer between 100 and 999 and adds all the digits in the integer. For example, if an integer is 932, the sum of all its digits is 14. 


x=input("enter a number between 0 and 100: ")
sum=0
for char in x:
    sum=int(char)+sum
print("the sum of the digits is: ", sum)