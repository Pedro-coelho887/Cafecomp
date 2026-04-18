from drinks import Drink
from drinks import HotDrink
from users import User
from data_storage import DataStorage
class CoffeeMachine():
    def __init__(self,storage):
        print("Bem vindo a Máquina de Bebidas!")
        self.ingredients_stock = {}
        self.__accountBalance = 0
        self.storage = storage
        self.is_on = True
        self.user = None

    def show_candrinks_stock(self):
        """Exibe o Estoque de bebidas em lata"""
        print("Estoque Atual:")
        for id in self.storage.candrinks_stock:
            print(f"{self.storage.candrinks_stock[id]["Descrição"]} Quantidade: {self.storage.candrinks_stock[id]["Quantidade"]} Preço: {self.storage.candrinks_stock[id]["Preço"]} ({id})")

    def financial_transaction(self):
        """Validação metodo de Pagamento e atualiza caixa"""
        payment_method = input(" Qual o modo de pagamento? \n Cartão de Crédito (CC) \n Cartão de Débito (CD)\n Pix (P) \n Selecionado:")
        if payment_method in ["CC","CD","P"]:
            print("Pagamento Aceito!")
            self.user.payment_method = payment_method #type:ignore
            self.__accountBalance += self.user.drink.price #type:ignore
            return True
        else:
            print("Metodo de pagamento inválido :( ")
            return False

    def buy_can(self):
        """Processo de compra de lata"""
        print("Selecione a bebida desejada:")
        self.show_candrinks_stock()
        drink_id = input("Código Bebida Desejada: ")
        if drink_id in self.storage.candrinks_stock and self.storage.candrinks_stock[drink_id]["Quantidade"] > 0:
            self.user.drink = Drink(name=self.storage.candrinks_stock[drink_id]["Descrição"],price=self.storage.candrinks_stock[drink_id]["Preço"],code=drink_id) #type:ignore
            sucess = self.financial_transaction()
            if sucess:
                self.storage.candrinks_stock[self.user.drink.code]["Quantidade"] -= 1 #type:ignore
                self.storage.update_candrinks_stock(self.user,self.__accountBalance)
                print(f"Aproveite seu {self.storage.candrinks_stock[drink_id]["Descrição"]}!")


    def client_intention(self):
        """Capta a inteção de compra do cliente e redireciona para a compra."""
        drink_type = input("O que deseja comprar? \n Bebida em lata (Bl) \n Café(C) \n Selecionado: ")
        if drink_type == "Bl":
            self.buy_can()

    def welcome(self):
        """TO DO: Loop principal da máquina"""
        self.is_on = True
        self.storage.read_candrinks_stock("data/candrinks_stock.txt")
        while self.is_on:
            username = input("Olá! Como devo chamá-lo?\n")
            self.user = User(name=username)
            user_type = input(f"Bem vindo {self.user.name}! Como posso ajudá-lo? \n Cliente(C) \n Administrador(A) \n Sair(E) \n Selecionado:")
            if user_type == "C":
                self.client_intention()
            elif user_type == "E":
                self.is_on = False

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


