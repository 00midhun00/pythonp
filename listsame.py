l1=[1,2,3,4]
l2=[2,3,4,1]

if len(l1) == len(l2):
    print("\n same lenght")

s1=0
s2=0
for i in l1:
    s1=s1+i
for i in l2:
    s2=s2+i
print(s1)
print(s2)

for i in l1:
    for j in l2:
        if i == j:
            print(i)

    