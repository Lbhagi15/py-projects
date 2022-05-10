#check the number is prime or not

n=int(input("enter the number :"))
c=0
i=1

while i<=n:
    if n%1==0:
        c+=1
    i+=1

    if c==2:
        print("prime")
    else:
        print("not prime")