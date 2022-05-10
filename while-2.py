# print the  factors of given number and their count

n=int(input("enter the number:"))
c=0
i=1
print('factors of{}: format(n)')
while i<=n:
    if n%i==0:
        print(i)
        c+=1
    i+= 1
print("factors cound:",c)

