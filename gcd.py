num1=int(input(":"))
num2=int(input(":"))
i=1
gcd=0
while (i<=num1 and i<=num2):
    if (num1 % i ==0 and num2 % i==0): #order matter
        gcd=i
    i=i+1
print(gcd) 

