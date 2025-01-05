class Employee:
    def __init__(self,name,id,dep,salary):
        self.name=name
        self.id=id
        self.dep=dep
        self.salary=salary

    def display(self):
        print(self.name)
        print(self.dep)
e1=Employee("a",20,"eco",10000)
e1.display()
         