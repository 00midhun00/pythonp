mark=[]
class Student:
    def __init__(self,rolno,name,mark):
        self.rno=rolno
        self.n=name
        self.m=mark
    def percentage(self):
        total=sum(self.m)
        totals=len(self.m)
        return (total/(totals*100)*100)

    def dispaly(self):
        print(self.rno)
        print(self.n)
        print(self.m)
        print(self.percentage())
n=input("enter the name:")
rno=int(input("enter the rono:"))
no=int(input("enter the no of sub:"))
for i in range(no):
    m=int(input("entere the mark:"))
    mark.append(m)
stu1=Student(rno,n,mark)
stu1.dispaly()

        