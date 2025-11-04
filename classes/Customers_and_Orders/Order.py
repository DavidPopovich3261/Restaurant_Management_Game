from classes.Customers_and_Orders.Customer import Customer


class Order:
    def __init__(self,customer:Customer,order_number):
        self.customer=customer
        self.order_number=order_number
        self.items=[]
        self.status='pending'
        self.total_price=0

    def add_item(self,menu_item):
        self.items.append(menu_item)
        self.total_price+=menu_item.price

    def remove_item(self,menu_item):
        if menu_item in self.items:
            self.items.remove(menu_item)
            self.total_price-=menu_item.price

    def get_total(self):
        return self.total_price

    def set_status(self,new_status):
        self.status=new_status

    def display_order(self):
        print(f"{self.order_number,self.customer.name,self.items,self.total_price,self.status}")

    def is_complete(self):
        if self.status=='delivered':
            return True
        return False
