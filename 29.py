# Write a program to find the roots of a given quadratic equation and print the nature of roots.
import cmath
a = int(input( "enter the first value :"))     # enter the input values through the keyboard
b = int(input("enter the second value:"))      # enter the input values through the keyboard
c = int (input("enter the third value:"))      # enter the input values through the keyboard

# calculating the discriminant value
discriminant_value = (b**2) - (4 * a*c)

# find  the roots of quadratic equation
ans1 = (-b - cmath.sqrt(discriminant_value))/(2 * a)
ans2 = (-b + cmath.sqrt(discriminant_value))/(2 * a)


# printing the roots of quadratic equatation
print('The roots are')
print(ans1)
print(ans2)
