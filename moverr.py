class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Book(Publisher):
    def __init__(self,title,author, name):
        super().__init__(name) 
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(self.author)
        print(self.title)
class Python(Book):
    def __init__(self, title, author, name,price,nop):
        super().__init__(title, author, name)
        self.price=price
        self.nop=nop
    def display(self):
        super().display()
        print(self.price)
        print(self.nop)
py=Python("a","B","python",100,200)
py.display()