# Write a program to find the simple interest and compound interest

principal = float(input("enter the principal amount"))      # entering the principal amount
tenure = float(input("enter the  tenure "))                 # entering the tenure period
rate = float(input("enter the   interest rate "))           # entering the interst
# calculating the simple interest
simple_interest = (principal*tenure*rate)/100

#calculating th compound interest
compound_interest = principal*(1+rate/100)**tenure-1

# printing the simple interest & compound interest
print(f"simple_interest of {principal},{tenure}and{rate} is {simple_interest}")
print(f"compound_ interest of {principal},{tenure}and{rate} is{compound_interest}")
print("The end")
