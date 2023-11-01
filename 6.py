# #taking inputs fromm user
# a = int(input(" Please Enter the First Value : "))
# b = int(input(" Please Enter the Second Value : "))
# #initialising
# i = 1
# #looping till the hcf/gcd is found
# while(i <= a and i <= b):
#     if(a % i == 0 and b % i == 0):
#         val = i
#     i = i + 1
# #displaying the hcf/gcd   
# print(f'The HCF/GCD of {a} and {b} is {val}')


n = int(input("Enter the number you want to take gcd of :-"))
count= 1
i=1
while count <=n:
    num = int(input("Enter a digit:- "))
    count+=1
if n <=0:
    print("Invalid input")
else:
    while n:
        num2=num
        num=n
        n=num2%n  
        i += 1
print(f"GCD of given numbers is {num}")