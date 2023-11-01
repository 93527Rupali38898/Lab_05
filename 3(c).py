N = int(input("enter a number:"))
i = 0
while i<=N:
    f = N
    while f>=0:
        b = (2*i)-1
        print(' '*f,'*'*b)
        f-=1
        i+=1