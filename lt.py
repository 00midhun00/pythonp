class Rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l * self.w
    def __lt__(self,other):
        if self.area() < other.area():
            return True
        else:
            return False
r1=Rect(10,20)
r2=Rect(20,30)

if r1 < r2:
    print("r2 area is gret")
else:
    print("r1 area is great")


        