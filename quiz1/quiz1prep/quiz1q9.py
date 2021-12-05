#If you know the balance and the annual percentage interest rate, you can compute the interest on the next monthly payment using the following formula:

text=input("the balance and interest are: ")

num=text.split(",")

balance, interest= int(num[0]), int(num[1])
print("the interest is: ", balance*(interest/1200))