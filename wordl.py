n=int(input("enter the limit:"))

w=[]

for i in range(n):
    wo=input("entert the word:")
    w.append(wo)
max=len(w[0])
temp=""

for i in w:
    if len(i) > max:
        max=len(i)
        temp=str(i)

print("the word is ",temp,"lenght is ",max)
