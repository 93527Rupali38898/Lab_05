N = int(input("enter a number:"))
if N<=0:
    print("invalid input")
else:
    i=1
    while i<=1000:
        if i%N!=0:
            print(i)
        i+=1