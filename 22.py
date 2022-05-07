# Write a program to print the area of a triangle if three sides are given.
# taken input from the user
a = float(input("enter the first side :"))
b = float(input("enter the second side :"))
c = float(input("enter the third value :"))
# fin out  the  semi-perimeter of triangel
s = (a+b+c)/2
# calculate the area of triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f" area of tringle  {s},{s-a},{s-b} and {s-c} is {area} ")