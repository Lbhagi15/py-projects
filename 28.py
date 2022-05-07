# Write a program to check whether the given year is leap year or not.
# checking if the  given nuber  leap year or not .
year = int(input("enter the year"))
if((year % 400 == 0)or(year % 100 != 0)and(year % 4 == 0)):
    print("Given year is a leap year")
# Else it is not a leap year.
else:
    print ("Given year is not a leap year")