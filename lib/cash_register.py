#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0, total=0,):
        self.total = total
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total = self.total + (price * quantity)
        self.last_transaction = (price * quantity)
        for num in range(quantity):
            self.items.append(title)
            

    def apply_discount(self):
        if self.total == 0:
            print("There is no discount to apply.")
        else:    
          self.total -= int(self.total * (self.discount / 100))
          print(f'After the discount, the total comes to ${self.total}.')

    def void_last_transaction(self):
        self.total = self.total - self.last_transaction
