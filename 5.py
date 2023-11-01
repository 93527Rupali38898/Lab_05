# #taking inputs from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1<0 or num2<0:
#     print("Please enter positive numbers")
# #checking the greater number  
# if(num1 > num2):
#     a = num1 
# else:
#     a=num2
# #looping till the a is found
# while(True):
#     if((a % num1 == 0) and (a % num2 == 0)):
#         print(f'The a of {num1} and {num2} is {a}')
#         break
#     a += 1

# N = int(input('enter number of integers:'))
# count = 0
# lcm=1
# while count<=N:
#     n = int(input('enter a number: '))
#     a,b=lcm,n
#     while n:
#         a,b=b,a%b
#         temp=a
#         lcm=(lcm*n)//temp
#         count+=1
# print(lcm)



n = int(input("count of number input wanted by the user"))

count = 1
lcm =1

while count<=n:
    num = int(input(f"enter a number{count}:-"))
    a, b = lcm, num
    while b:
        a,b=b,a%b
    temp=a 
    lcm = (lcm * num) // temp
    count+= 1

print(f"LCM of given numbers is {lcm}")