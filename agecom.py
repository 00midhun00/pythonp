class Person:
    def __init__(self,n,a):
        self.n=n
        self.a=a
p1=Person("a",18)
p2=Person("b",25)

if p1.a >p2.a:
    print(p1.a,"is great")
elif p2.a >p1.a:
    print(p2.a,"is graet")
else:
    print("age is equal")
        