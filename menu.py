class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

class Menu:
    def __init__(self):
        self.menu_items = {
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        }

    def get_items(self):
        """Returns a string with names of available drinks"""
        return ", ".join([item.name for item in self.menu_items])
    
    def find_drink(self, drink_name):
        """Search for a drink by name and return it if found"""
        for item in self.menu_items:
            if item.name == drink_name:
                return item
        return None