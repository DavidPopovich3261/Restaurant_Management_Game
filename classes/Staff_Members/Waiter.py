from classes.Staff_Members.Staff import Staff
from classes.Customers_and_Orders.Order import Order


class Waiter(Staff):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.tips=0

    def take_order(self,customer, menu,order_number):
        order=Order(customer,order_number)
        menu.display_menu()
        name=input("")
        item=menu.get_item_by_name(name)
        order.add_item(item)
        order.display_order()
        return order

    def serve_order(self, order:Order):
        order.status='delivered'
        order.customer.get_info()

    def receive_tip(self,amount):
        self.tips+=amount

    def get_total_earnings(self):
        return f"{self.salary+self.tips}"




