user_choice = input("what would you like? (espresso/latte/cappuccino):")
# User can enter: espresso/latte/cappuccino/off/report

resources = {'water':100, 'milk':150, 'coffee':200, 'money':0.00}

espresso = {'water':12, 'milk':10, 'coffee':7, 'money':2.50}
latte = {'water':10, 'milk':15, 'coffee':5, 'money':1.50}
cappuccino = {'water':15, 'milk':10, 'coffee':4, 'money':2.00}

isOff = False
if user_choice == 'off':
    isOff = True

def report():
    print(f"\nReport\n\n************\nWater: {resources['water']}ml\n Milk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}\n************")

if user_choice == 'report':
    report()

def checkResourceSufficient(whichCoffee):
    if resources['water']>=whichCoffee['water'] and resources['milk']>=whichCoffee['milk'] and resources['coffee']>=whichCoffee['coffee']:
        return True
    else:
        if resources['water']<whichCoffee['water']:
            print("Sorry, there is not enough water")
        elif resources['milk']<whichCoffee['milk']:
            print("Sorry, there is not enough milk")
        else:
            print("Sorry, there is not enough coffee")
        return False
        
coin_values = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}

def amountToBePaid(choice):
    if choice == 'espresso':
        amount = input(f"Please pay ${espresso['money']}")
        if amount == espresso['money']:
            return True
    elif choice == 'latte':
        amount = input(f"Please pay ${latte['money']}")
        if amount == latte['money']:
            return True
    else:
        amount = input(f"Please pay ${cappuccino['money']}")
        if amount == cappuccino['money']:
            return True
    return False
    
if(amountToBePaid(user_choice) == False):
    print("“Sorry that's not enough money. Money refunded.")

