from drinks import Drink
from drinks import HotDrink
from users import Admin
from users import User
class CoffeeMachine:
    def __init__(self):
        print("Bem vindo a Máquina de Bebidas!")
        self.coffee_stock = 5
        self.sugar_stock = 5
        self.milk_stock = 5
        self.drinks_stock = {"(Sl)":[5,"Suco de Laranja"],"(R)":[0,"Refrigerante"]}
        self.accountBalance = 0
        self.is_on = True

    # def transaction(self,user,drink):
    #     """TO DO: Desconta Drink Pedido pelo Cliente, atualiza saldo"""
    #     pass
    
    def select_hot_drink(self):
        print("Escolha uma opção de bebida no estoque:")
        for drink in self.drinks_stock:
            print(f"{self.drinks_stock[drink][1]} {drink} Disponível: {self.drinks_stock[drink][0]} \n")
        print("\n Aperte E para sair \n")
        drink_opt = input("Bebida escolhida:")

        return drink_opt
    
    def financial_transaction(self,id):
        payment_method = input(" Qual o modo de pagamento? \n Cartão de Crédito (CC) \n Cartão de Débito (CD)\n Pix (P)")
        if payment_method in ["CC","CD","P"]:
            print("Pagamento Aceito!")
            return True
        else:
            print("Metodo de pagamento inválido :( )")
            return False
        
    def give_hot_drink(self,id):
        self.accountBalance += 10
        self.drinks_stock[id][0] -= 1
        print("Aproveite sua bebida!")

    def valid_admin(self):
        """TO DO: Validar que o usuário é Admin"""
        pass
    
    def admin_options(self):
        """TO DO: Retorna Opção selecionada pelo Admin (Reabastecer, Cadastrar Produto ou Tirar Dinheiro)"""
        pass

    def fill_ingredients(self):
        """TO DO: Admin reabastece máquina"""
        pass

    def withdraw_money(self):
        """TO DO: Admin Retira dinheiro"""
        pass

    def new_product(self):
        """TO DO: Admin Cadastra Produto --Deixar para depois de implementado banco de dados"""
        pass

    def dose_drink(self):
        """TO DO: Dosa o drink do usuário"""


