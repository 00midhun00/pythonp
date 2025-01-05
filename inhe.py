class A:
    def __init__(self):
         print("\n A")
    def f1(self):
         print("f1 A")
class B:
     def __init__(self):
          print("\n B")
          super().__init__()
     def f2(self):
          print("in f1 B")
class c(B,A):
     def __init__(self):
          super().__init__()
          print("C")
     def f3(self):
          print("in f3 C")
ob=c()
ob.f3()