class Vh:
    wheel=4
    def __init__(self,m,c):
        self.m=m
        self.c=c
    def dis(self):
        print(self.m)
        print(self.c)
        print(__class__.wheel)
v=Vh(220,"toyota")
v.dis()
        