import numpy as np

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        item_info = {'name':name, 'price':price}
        for i in range(quantity):    
            self.items.append(item_info)
        self.total += price*quantity
        return self.total
    
    def mean_item_price(self):
        return(f"The mean price is {self.total/len(self.items)}")

    def median_item_price(self):
        prices_list = []
        prices_list = [item['price'] for item in self.items]
        length = len(prices_list)
        half = int(length/2)
        prices_list.sort()
        if length % 2 == 0:
            return(f"The median price is {(prices_list[half-1]+prices_list[half])/2}")
        else:
            return(f"The median price is {prices_list[half]}")
        
    def apply_discount(self):
        discount_total = None
        if self.employee_discount:
            discount_total = self.total * (1 - (self.employee_discount/100))
            return(discount_total)
        else:
            return("Sorry, there is no discount to apply to your cart :(")

    def void_last_item(self):
        if not self.items:
            return("There are no items in your cart!")
        else:
            removed_item = self.items.pop()
            self.total -= removed_item['price']
            return(self.total)
            