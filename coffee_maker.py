class CoffeeMaker:
    def __init__(self, water=300, milk=200, coffee=100):
        self.resources = {
            "water" : water,
            "milk" : milk,
            "coffee" : coffee
        }
    
    def report(self):
        print(f"************\nReport\n************")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resource_check_message(self, drink):
        messages = []
        if self.resources["water"] < drink.water:
            messages.append("Sorry, not enough water.")
        if self.resources["milk"] < drink.milk:
            messages.append("Sorry, not enough milk.")
        if self.resources["coffee"] < drink.coffee:
            messages.append("Sorry, not enough coffee.")
        return messages


    def is_resource_sufficient(self, drink):
        messages = self.resource_check_message(drink)
        if messages:
            for message in messages:
                print(message)
            return False
        return True
        
    def make_coffee(self, drink):
        if self.is_resource_sufficient(drink):
            self.resources["water"] -= drink.water
            self.resources["milk"] -= drink.milk
            self.resources["coffee"] -= drink.coffee
            print(f"Here is your {drink.name}. Enjoy!")
