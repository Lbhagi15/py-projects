n = int(input("enter the number"))
c = 0
i = 2
rt = int(n**0.5)
while i <= rt:
    c += 1
    i += 1

    if c == 0:
        print("prime")
    else:
        print("not  prime")

