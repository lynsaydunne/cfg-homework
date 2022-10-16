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
        self.total_items = {}
        self.total_price = 0.00
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item] = price
        self.total_price = self.total_price + price

    def remove_item(self, item):
        price = self.total_items.pop(item)
        self.total_price = self.total_price - price

    def apply_discount(self, discount_amount):
        self.discount += discount_amount

    def get_total(self):
        return max(self.total_price - self.discount, 0)

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"You have {item} that costs £{price:.2f}")
        print(f"Your total is £{self.total_price:.2f}")
        print(f"Your discount comes to: £{self.discount:.2f}")
        print(f"Your final total is £{self.get_total():.2f}")

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0


if __name__ == '__main__':
    # my_list = ['cat', 'dog', 'sheep']
    my_cash_register = CashRegister()
    # print(my_cash_register.total_items)
    # print(my_cash_register.total_price)
    my_cash_register.add_item('bananas', 1.00)
    my_cash_register.add_item('kiwi', 1.50)
    my_cash_register.add_item('green beans', 0.75)
    print(my_cash_register.total_items)
    print(my_cash_register.get_total())
    my_cash_register.remove_item('kiwi')
    print(my_cash_register.total_items)
    print(my_cash_register.get_total())
    my_cash_register.apply_discount(1.00)
    print(my_cash_register.get_total())
    my_cash_register.show_items()
    my_cash_register.reset_register()
    print(my_cash_register.total_items)

