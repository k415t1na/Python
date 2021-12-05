#Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water. 

m=float(input("enter amount of water in kilos: "))
initialTemperature=float(input("enter the initial temp: "))
finalTemperature=float(input("enter the final temp: "))



print("the energy: ", m*(finalTemperature-initialTemperature)*4184 )