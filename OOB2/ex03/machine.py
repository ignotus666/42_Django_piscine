import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.served_count = 0

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            # Returns a temporary object from Exception class. Allows you access to their methods without naming it.
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.served_count = 0

    def serve(self, beverage: HotBeverage):
        if self.served_count >= 10:
            raise self.BrokenMachineException()
        
        self.served_count += 1
        if random.randint(0, 1) == 0:
            return beverage()
        return self.EmptyCup()

if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages_list = [Coffee, Tea, Chocolate, Cappuccino]

    print("--- First round of coffee! ---")
    for _ in range(2):
        try:
            while True:
                drink = machine.serve(random.choice(beverages_list))
                print(drink)
                print("--------------------")
        except CoffeeMachine.BrokenMachineException as e:
            print(f"\n[ERROR] {e}")
            print("Repairing the machine...\n")
            machine.repair()
