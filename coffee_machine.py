from drinks import Drink
from drinks import HotDrink
from users import User
from data_storage import DataStorage
class CoffeeMachine():
    def __init__(self,storage:DataStorage):
        print("Bem vindo a Máquina de Bebidas!")
        self.storage = storage
        self.__accountBalance = self.storage.get_actual_accountbalance("data/transactions.txt")
        self.is_on = True
        self.user = None

    def show_candrinks_stock(self):
        """Exibe o estoque de bebidas em lata"""
        print("Estoque Atual:")
        for id in self.storage.candrinks_stock:
            print(f"{self.storage.candrinks_stock[id]["Descrição"]} Quantidade: {self.storage.candrinks_stock[id]["Quantidade"]} Preço: {self.storage.candrinks_stock[id]["Preço"]} ({id})")

    def show_ingredients_stock(self):
        """Exibe o estoque de ingredients """
        print("Estoque Atual:")
        for ingredient in self.storage.ingredients_stock:
            print(f"{ingredient}     {self.storage.ingredients_stock[ingredient]}")

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
            success = self.financial_transaction()
            if success:
                self.storage.candrinks_stock[self.user.drink.code]["Quantidade"] -= 1 #type:ignore
                self.storage.update_candrinks_stock(self.user,self.__accountBalance)
                print(f"Aproveite seu {self.storage.candrinks_stock[drink_id]["Descrição"]}!")

    def buy_dosed_drink(self):
        """Processo de compra de bebida dosada"""
        self.show_ingredients_stock()
        coffee = int(input("Qual a quantidade de café desejada? (Máximo 10)"))
        while 0 > coffee or coffee > 10 or coffee > self.storage.ingredients_stock["Coffee"]:
            print("Quantidade Inválida!")
            coffee = int(input("Qual a quantidade de café desejada? (Máximo 10)"))

        milk = int(input("Qual a quantidade de leite desejada? (Máximo 10)"))
        while 0 > milk or milk > 10 or milk > self.storage.ingredients_stock["Milk"]:
            print("Quantidade Inválida!")
            milk = int(input("Qual a quantidade de leite desejada? (Máximo 10)"))

        sugar = int(input("Qual a quantidade de açúcar desejada? (Máximo 10)"))
        while 0 > sugar or sugar > 10 or sugar > self.storage.ingredients_stock["Sugar"]:
            print("Quantidade Inválida!")
            sugar = int(input("Qual a quantidade de açúcar desejada? (Máximo 10)"))
        
        self.user.drink = HotDrink(name="Coffee",price=10,code="C",coffee=coffee,milk=milk,sugar=sugar) #type:ignore
        success = self.financial_transaction()
        if success:
            self.storage.ingredients_stock["Coffee"] -= coffee
            self.storage.ingredients_stock["Milk"] -= milk
            self.storage.ingredients_stock["Sugar"] -= sugar
            self.storage.update_ingredients_stock(self.user,self.__accountBalance)
            print("Aproveite seu Café!")

    def client_intention(self):
        """Capta a inteção de compra do cliente e redireciona para a compra."""
        drink_type = input("O que deseja comprar? \n Bebida em lata (Bl) \n Café(C) \n Selecionado: ")
        if drink_type == "Bl":
            self.buy_can()
        elif drink_type == "C":
            self.buy_dosed_drink()

    def valid_admin(self):
        """TO DO: Validar que o usuário é Admin"""
        pass

    def welcome(self):
        """TO DO: Loop principal da máquina"""
        self.is_on = True
        self.storage.read_candrinks_stock("data/candrinks_stock.txt")
        self.storage.read_ingredients_stock("data/ingredients_stock.txt")
        while self.is_on:
            username = input("Olá! Como devo chamá-lo?\n")
            self.user = User(name=username)
            user_type = input(f"Bem vindo {self.user.name}! Como posso ajudá-lo? \n Cliente(C) \n Administrador(A) \n Sair(E) \n Selecionado:")
            if user_type == "C":
                self.client_intention()
            elif user_type == "A":
                self.valid_admin()
                #self.admin_intention()
            elif user_type == "E":
                self.is_on = False
            else:
                print("Selecione uma opção válida")

    
    
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


