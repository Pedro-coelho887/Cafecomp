from drinks import Drink
from drinks import HotDrink
class User:
    def __init__(self,permission=None,name=None,drink:Drink | None = None,payment_method:str | None = None):
        self.name = name
        self.permission = permission
        self.drink = drink
        self.payment_method = payment_method


