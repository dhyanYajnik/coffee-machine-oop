class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.coin_values = {
            'quarters': 0.25, 
            'dimes': 0.1, 
            'nickels': 0.05, 
            'pennies': 0.01
        }

    def report(self):
        print(f"Money: ${self.profit:.2f}")
    
    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("Enter quarters: ")) * self.coin_values['quarters']
        dimes = int(input("Enter dimes: ")) * self.coin_values['dimes']
        nickels = int(input("Enter nickels: ")) * self.coin_values['nickels']
        pennies = int(input("Enter pennies: ")) * self.coin_values['pennies']

        total_amount = quarters + dimes + nickels + pennies
        return total_amount

    def is_transaction_successful(self, amount_recieved, drink_cost):
        if amount_recieved >= drink_cost:
            change = round(amount_recieved - drink_cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            self.profit += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

