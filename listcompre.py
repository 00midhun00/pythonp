#to show positive numbers
l1=[1,-1,2,-3,4]
l2=[x for x in l1 if x>0]
print(l2)
#to square from list
l1=[]
l2=[]
n=int(input("enter the no of ele:"))

for i in range(n):
    num=int(input("enter the numbers:"))
    l1.append(num)
print(l1)
l2=[x*2 for x in l1]
print(l2)
#to show vwel
w=input("enter word:")
vow=[x for x in w.lower() if x in ["a","e","i","o","u"]]
print(w)
print(vow)
#to show ordinal values

w=input("enter the word:")
ord=[ord(i) for i in w]
print(ord)