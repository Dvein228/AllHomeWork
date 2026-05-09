class Student:
    def __init__(self,name,age,money,study):
        self.name = name
        self.age = age
        self.money = money
        self.study= study
    def work(self):
        self.money+=1
        self.study-=1
        if self.money>0 and self.study>0:
            self.relax()
    def relax(self):
        self.money-=1
        self.study-=10
        if self.money<0:
            self.work()
        if self.study<0 and self.money<0:
            self.backStudy()
    def backStudy(self):
        self.study+=1

