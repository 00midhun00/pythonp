import math
perfect=[]
num1=int(input("enter the start:"))
num2=int(input("enter the end:"))

for i in range(num1,num2+1):
    flag=0
    num=i
    while num > 0:
        digit=num%10

        if digit not in [0,2,4,6,8]:
            flag=1
        num=int(num/10)
    if flag==0 and math.sqrt(i) %1==0:
        perfect.append(i)
print(perfect)