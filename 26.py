# Write a program to find smallest of given two numbers.
num1 = float(input("enter first number:"))
num2= float(input("enter second number:"))

# checking the smallest of two numbers

if ( num1 < num2 ) :
    smallest = num1
else:
    smallest = num2
# printing the smallest number of two number

print("The smallest  number is", smallest)