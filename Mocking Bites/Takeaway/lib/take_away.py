class Menu:
    def __init__(self):

        self.menu_items = {}

    def add_dish(self, item: str, price: float):
        
        self.menu_items[item] = price

    def return_list(self):
        
        return self.menu_items


class OrderDish:
    def __init__(self, item: str, quant: int, price: float):
        
        self.item = item
        self.quant = quant
        self.price = price

    def subtotal(self):
    
        return self.quant * self.price


class Order:
    def __init__(self, menu: Menu):
        
        self.menu = menu
        self.items = []

    def add_dish(self, item: str, quant: int):
        
        if item in self.menu.menu_items:
            price = self.menu.menu_items[item]
            order_item = OrderDish(item, quant, price)
            self.items.append(order_item)

    def calculate_total(self):
        
        total = sum(item.subtotal() for item in self.items)
        return total

    def return_receipt(self):
        
        receipt = "Receipt:\n"
        for item in self.items:
            receipt += f"{item.item}: {item.quant} x ${item.price} = ${item.subtotal()}\n"
        receipt += f"Total: ${self.calculate_total()}"
        return receipt


class Customer:
    def __init__(self, order: Order, requester):
        self.order = order
        self.requester = requester

    def order_place(self, dishes_quantities):
        for dish, quantity in dishes_quantities.items():
            self.order.add_dish(dish, quantity)
            print(dishes_quantities)
        self.confirm()

    def confirm(self):
        response = self.requester.get("http://example.com/myapp")
        return response.json()




