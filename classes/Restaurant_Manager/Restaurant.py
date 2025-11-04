from classes.Menu_Items.Menu import Menu
from classes.Staff_Members.Staff import Staff
from classes.Staff_Members.Waiter import Waiter
from classes.Staff_Members.Chef import Chef
from classes.Customers_and_Orders.Order import Order


class Restaurant:
    def __init__(self,name):
        self.name=name
        self.menu=Menu()
        self.staff=[]
        self.orders=[]
        self. money =1000
        self.order_number=0

    def hire_staff(self,staff_member):
        self.staff.append(staff_member)

    def fire_staff(self,staff_name):
        for i in self.staff:
            if i.name==staff_name:
                self.staff.remove(i)

    def create_order(self,customer):
        for i in self.staff:
            if isinstance(i,Waiter):
                self.order_number += 1
                order=i.take_order(customer,self.menu,self.order_number)

                self.orders.append(order)
            return

    def process_order(self,order:Order):
        for i in self.staff:
            if isinstance(i,Chef):
                i.cook_order(order)
            if isinstance(i,Waiter):
                i.serve_order(order)
            return

    def complete_order(self,order):
        self.money+=order.total_price
        self.orders.remove(order)

    def pay_salaries(self):
        for i in self.staff:
            self.money-=i.salary

    def get_statistics(self):
        statistics={'orders':len(self.orders),'money':self.money,'staff':len(self.staff),'total orders':self.order_number }
        return statistics



