li=[]
lim=int(input("enter the limit"))
sum=0
print("enter ",lim ,"numbers")
for i in range(lim):
    li1=int(input())
    li.append(li1)
print(li)
for i in li:
    sum=sum+i
print(sum)