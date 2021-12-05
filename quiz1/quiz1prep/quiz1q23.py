#Write a python program to ask the user to enter 3 numbers. Check whether those can be the sides of isosceles triangle (a == b, b != c).

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y and y!= z:
	print("Isosceles triangle")

else:
	print("Not an isosceles")