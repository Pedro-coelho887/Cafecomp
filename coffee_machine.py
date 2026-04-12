from drinks import Drink
from drinks import HotDrink
from users import Admin
from users import User
class CoffeeMachine:
    def __init__(self):
        self.coffee_stock = 0
        self.sugar_stock = 0
        self.milk_stock = 0
        self.currentCash = 0
        self.accountBalance = 0

    def fill_ingredients(self,user,coffee,sugar,milk,drinks):
        """TO DO: Admin reabastece máquina"""
        pass

    def transaction(self,user,drink):
        """TO DO: Desconta Drink Pedido pelo Cliente, atualiza saldo"""
        pass

