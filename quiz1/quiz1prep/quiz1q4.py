#Write a program that reads in the radius and length of a cylinder and computes the area and volume using the following formulas:area = radius * radius * πvolume = area * length
import math

rad=float(input("enter the radius: "))
length=float(input("enter the length: "))

area=rad*rad*math.pi
print("the area is: ", area)
print("the volume is: ", area * length)