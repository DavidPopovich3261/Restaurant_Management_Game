from os import remove

from classes.Menu_Items.MenuItem import MenuItem

class Menu:
    def __init__(self):
        self.items=[]

    def add_item(self,menu_item):
        self.items.append(menu_item)

    def remove_item(self,item_name):
        for i in self.items:
            if i.name==item_name:
                self.items.remove(i)

    def get_item_by_name(self,name):
        for i in self.items:
            if i.name==name:
                return i

    def get_items_by_category(self,category):
        list_items=[]
        for i in self.items:
            if i.category==category:
                list_items.append(i)
        return list_items

    def display_menu(self):
        print(f"=====menu=====")
        for x,y in enumerate( self.items):
            print(f"{y}.{x}")

    def get_total_items(self):
        return len(self.items)