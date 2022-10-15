"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.total_items.append(item)

    def remove_item(self, item):
        self.total_items.remove(item)

    def apply_discount(self, discount_percentage):
        discount_amount = self.total_price * discount_percentage
        self.discount += discount_amount
        print("Discount Applied")

    def get_total(self):
        self.total_price = 0
        for item_price in self.total_items.values():
            self.total_price += item_price

    def show_items(self, item):
        print(self.total_items(item))

    def reset_register(self):
        pass

add_item('bananas')
