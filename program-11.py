# Write a program to convert speed of a vehicle given in km/hour to miles/hour.
# entering the kilometers through keybord
kilometers=float(input("enter the kilometrs value"))

# the converting  factor is

conv_fac= 0.621371

# converting the  km/hour to miles/hour
miles= kilometers *conv_fac

# printing the miles...
print(f"miles of {kilometers},{conv_fac} of {miles}")
