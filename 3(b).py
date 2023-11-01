N = int(input("enter a number:"))
i = 1
while i<=N:
    f = N
    while f>=0:
        print(' '*f,'*'*i)
        f-=1
        i+=1