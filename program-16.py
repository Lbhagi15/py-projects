#Given the coordinates of two points (x1, y1) and (x2, y2). Write a program to find
#the distance between these two points
# import the math function
import math
#take the input  from users
x1 = int(input(" enter the x1  value"))
y1 = int (input("enter the y1 value"))
x2 = int(input(" enter the x2 value"))
y2 = int(input("enter the y2 value"))

# calculating the distance between these two points
distance = math.sqrt(pow(x2 - x1, 2) +pow(y2 - y1, 2))

# printing the distance blw two ponts
print(f"distance of {x1},{y1},{x2},{y2} of {distance}"