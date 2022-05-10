n=int(input("enter the n value:"))
c = 0
i = 2

while i <= n//2:

     if n %i == 0:
        c += 1
     i += 1

if c == 0:

    print("prime")
else:
    print("not prime")


