class Time:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s
    def __add__(self,other):
        h=self.__h+other.__h
        m=self.__m+other.__m
        s=self.__s+other.__s

        if s >=60:
            s=s+int(s/60)
            s=s%60
        if m>=60:
            m=m+int(m/60)
            m=m%60
        t3=Time(h,m,s)
        return t3
    def display(self):
        print(self.__h)
        print(self.__m)
        print(self.__s)
t1=Time(1,60,60)
t2=Time(1,60,60)
t3=t1+t2
t3.display()

        