first=0
second=1

lim=int(input("enter the limit"))
print(first)
print(second)
for i in range(lim-2):
    third=first+second
    first=second
    second=third
    print(third)