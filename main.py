from coffee_machine import CoffeeMachine
from data_storage import DataStorage
def main():
    storage = DataStorage()
    machine = CoffeeMachine(storage)
    machine.welcome()

if __name__ == "__main__":
    main()