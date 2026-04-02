import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.drinks_served = 0
        print("**Technician kicks machine** Coffee Machine repaired!")

    def serve(self, beverage_class):
        if self.drinks_served >= 10:
            raise self.BrokenMachineException()
        self.drinks_served += 1
        surprise_drink = random.randint(0, 1)
        if surprise_drink == 0:
            return self.EmptyCup()
        return beverage_class()
        
if __name__ == "__main__":
    shittyMachine = CoffeeMachine()
    drinks = [beverages.Coffee,
              beverages.Tea,
              beverages.Chocolate,
              beverages.Cappuccino]
    repairs = 0
    drink_counter = 0
    while repairs <= 1:
        try:
            for drink in drinks:
                drink = shittyMachine.serve(drink)
                print(f"{drink_counter + 1}\n{drink}")
                print("-" * 40)
                drink_counter += 1
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            if repairs == 0:
                print("Repairing coffee machine")
                shittyMachine.repair()
            repairs += 1
            drink_counter = 0