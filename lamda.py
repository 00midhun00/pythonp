a=int(input("enter the side"))
area=lambda a:a*a
print(area(a))

l=int(input("enter the length:"))
b=int(input("entert the bredth:"))
area=lambda l,b:l*b
print("arera of rectangle:",area(l,b))

h=int(input("entert h:"))
b=int(input("enter th b"))
area=lambda h,b:0.5*b*h
print("area triangle",area(h,b))