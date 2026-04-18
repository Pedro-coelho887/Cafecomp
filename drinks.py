# Bebidas Gerais
class Drink():
    def __init__(self,name:str,price:float,code:str):
        self.name = name
        self.code = code
        self.price = price

# Bebidas Dosadas
class HotDrink(Drink):
    def __init__(self,name,price,code):
        super().__init__(name,price,code)
        self.coffee = 0
        self.sugar = 0
        self.milk = 0

    def user_dose(self,coffee,sugar,milk):
        """TO DO: Adiciona as quantidades digitadas pelo usuário na bebida"""
        pass
        

