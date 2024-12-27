from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
    
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if drink and coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.process_coins()
            if money_machine.is_transaction_successful(payment, drink.cost):
                coffee_maker.make_coffee(drink)
