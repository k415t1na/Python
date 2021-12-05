#Ask the user to enter a number in the range [1,9]. If the user enters something invalid, keep asking for a number in that range. If the number is valid, print the multiplications for that number from 1 to 9:


n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,10):
   print(n,'x',i,'=',n*i)
   