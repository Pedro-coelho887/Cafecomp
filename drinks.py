# Bebidas Gerais
class Drink():
    def __init__(self,name:str,price:float,code:str):
        self.name = name
        self.code = code
        self.price = price

# Bebidas Dosadas
class HotDrink(Drink):
    def __init__(self,name,price,code,coffee,sugar,milk):
        super().__init__(name,price,code)
        self.coffee = coffee
        self.sugar = sugar
        self.milk = milk
        
        

