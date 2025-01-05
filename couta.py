n=int(input("enter the limit:"))
li=[]
c=0

print("enter the names:")
for i in range(n):
    na=input()
    li.append(na)
for i in li:
    for j in i:
        if "a" in j.lower():
            c=c+1

print(c)