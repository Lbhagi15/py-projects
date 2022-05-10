# Write a program to find the volume of a cylinder
# enter the input through keybord

PI = 3.14
radius = float(input("enter the  radius  of cylinder :"))
height = int(input("enter the height of cylinder:"))
# calculating the volume cylinder

volume = (PI * radius * radius * height)
print(f"volume of cylinder of {PI},{radius}and {height} is {volume}")
print("The End")