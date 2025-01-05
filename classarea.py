class Rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2*(self.w + self.l)

l=int(input("entert the l:"))
w=int(input("enter the w:"))    
r1=Rect(l,w)
print(r1.area())

l=int(input("entert the l:"))
w=int(input("enter the w:"))    
r2=Rect(l,w)
print(r2.area())

are1=r1.area()
are2=r2.area()

if are1 > are2:
    print(are1 ,"is great")
else:
    print(are2,"is grater")
        