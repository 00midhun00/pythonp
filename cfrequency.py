str=input("enter the charecter:")
print(len(str))
c=0
for i in range(len(str)):
    if str[i]!="":
        c=c+1
print(c)
