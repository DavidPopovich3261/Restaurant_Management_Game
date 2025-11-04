
class Staff:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.energy=100

    def work(self):
        self.energy-=10
        print("working")

    def rest(self):
        self.energy+=10

    def is_tired(self):
        if self.energy<30:
            return True
        return False

    def get_info(self):
        return f"{self.name,self.salary,self.energy}"
