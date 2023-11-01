N = int(input("enter N :"))
num = 0
n1 = 0
n2 = 0
while num != -999:
    num = int(input("enter numbers repeatedly:"))
    n1 += 1
    if num%N == 0:
        n2 += 1
# n1 -= 1
print("total numbers =",n1)
print("total numbers divisible by N =", n2)

