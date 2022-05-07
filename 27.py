# Write a program to find biggest of given three numbers.
num1 = float(input("enter first number:"))
num2= float(input("enter second number:"))
num3 = float(input("enter  third number:"))
# checking the largest of three numbers

if (num1 > num2) and (num1 > num3):
    biggest = num1
elif (num2 > num1) and (num2 > num3):
    biggest = num2
else:
    biggest = num3

print("The largest number is",biggest)