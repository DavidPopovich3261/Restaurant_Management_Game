class Customer:
    def __init__(self,name):
        self.name=name
        self.satisfaction=50

    def increase_satisfaction(self,amount):
        if self.satisfaction+amount<100:
            self.satisfaction+=amount
        else:
            self.satisfaction=100

    def decrease_satisfaction(self,amount):
        if self.satisfaction-amount>0:
            self.satisfaction-=amount
        else:
            self.satisfaction=0

    def is_happy(self):
        if self.satisfaction>=70:
            return True
        return False

    def get_info(self):
        return f"{self.name,self.satisfaction}"



