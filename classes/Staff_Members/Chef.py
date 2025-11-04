from classes.Staff_Members.Staff import Staff


class Chef(Staff):
    def __init__(self,name,salary,attribute):
        super().__init__(name,salary)
        self.attribute=attribute

    def cook_order(self,order):
        order.status='cooking'
        order.status='ready'
        self.override_work()

    def override_work(self):
        self.energy-=15
