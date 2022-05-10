#Write a program to find the area and circumference of a circle.
# enter the values throught the keybord
PI=3.14
radius = float(input( "enter the number"))

# calculating the circumference of circle
circumference=(2*PI*radius)

# calculating the area of  the circle
area=(PI*radius*radius)

#printing the circumferance & area of the circle
print(f" circumferance of{PI},{radius} of {circumference}")
print(f"area of {PI},{radius}and{radius} of {area}")
print("The End")