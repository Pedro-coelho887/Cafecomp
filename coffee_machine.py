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
        print("Preço: 10.00")
        self.show_ingredients_stock()
        coffee = int(input("Qual a quantidade de café desejada? (0, 3, 5, 7, ou 10 gramas)"))
        while 0 > coffee or coffee > 10 or coffee > self.storage.ingredients_stock["Café"]:
            print("Quantidade Inválida!")
            coffee = int(input("Qual a quantidade de café desejada? (0, 3, 5, 7, ou 10 gramas)"))

        milk = int(input("Qual a quantidade de leite desejada? (0, 3, 5, 7, ou 10 gramas)"))
        while 0 > milk or milk > 10 or milk > self.storage.ingredients_stock["Leite"]:
            print("Quantidade Inválida!")
            milk = int(input("Qual a quantidade de leite desejada? (0, 3, 5, 7, ou 10 gramas)"))

        sugar = int(input("Qual a quantidade de açúcar desejada? (0, 3, 5, 7, ou 10 gramas)"))
        while 0 > sugar or sugar > 10 or sugar > self.storage.ingredients_stock["Açúcar"]:
            print("Quantidade Inválida!")
            sugar = int(input("Qual a quantidade de açúcar desejada? (0, 3, 5, 7, ou 10 gramas)"))
        
        self.user.drink = HotDrink(name="Coffee",price=10,code="C",coffee=coffee,milk=milk,sugar=sugar) #type:ignore
        success = self.financial_transaction()
        if success:
            self.storage.ingredients_stock["Café"] -= coffee
            self.storage.ingredients_stock["Leite"] -= milk
            self.storage.ingredients_stock["Açúcar"] -= sugar
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
        """Valida que o usuário é Admin"""
        if self.user.name in self.storage.admins.keys(): #type:ignore
            password = input("Digite a sua senha de administrador: ")
            if self.storage.admins[self.user.name] == password: #type:ignore
                return True
            
        print("Autenticação inválida")
        return False

    def refill_candrinks(self):
        if self.user is not None and self.user.permission == False:
            print("Usuário sem permissão válida!")
            return
        candrink_code = input("Qual bebida deseja abastecer? (Digite o código)")
        if candrink_code not in self.storage.candrinks_stock.keys():
            print("Código de bebida inválido!")
            return

        quantity = int(input("Quantas unidades serão repostas?"))
        self.storage.candrinks_stock[candrink_code]["Quantidade"] += quantity
        self.storage.update_candrinks_stock(selling=False)
        print("Reposição feita com sucesso!")
        
    def refill_ingredients(self):
        if self.user is not None and self.user.permission == False:
            print("Usuário sem permissão válida!")
            return
        new_coffee = int(input("Quanto de Café deseja abastecer?"))
        new_sugar  = int(input("Quanto de Açúcar deseja abastecer?"))
        new_milk = int(input("Quanto de Leite deseja abastecer?"))
        self.storage.ingredients_stock["Café"] += new_coffee
        self.storage.ingredients_stock["Leite"] += new_milk
        self.storage.ingredients_stock["Açúcar"] += new_sugar
        self.storage.update_ingredients_stock(selling=False)
        print("Reposição feita com sucesso!")


    def admin_intention(self):
        """Capta a intenção do administrador"""
        admin_option = ""
        while admin_option != "E":
            admin_option = input(f"Olá {self.user.name}! O que deseja fazer? \n Reabastecer Bebidas em Lata (Rl)\n Reabastecer Ingredientes de Café (Ri)\n Ver estatísticas (S)\n Sair (E)\n") #type:ignore
            if admin_option == "Rl":
                self.show_candrinks_stock()
                self.refill_candrinks()

            elif admin_option == "Ri":
                self.show_ingredients_stock()
                self.refill_ingredients()

            elif admin_option == "S":
                self.storage.show_stats("data/transactions.txt")

            elif admin_option != "E":
                print("Selecione uma operação válida!")




    def welcome(self):
        """TO DO: Loop principal da máquina"""
        self.is_on = True
        self.storage.read_candrinks_stock("data/candrinks_stock.txt")
        self.storage.read_ingredients_stock("data/ingredients_stock.txt")
        self.storage.get_admins("data/admins.txt")
        while self.is_on:
            username = input("Olá! Como devo chamá-lo?\n")
            self.user = User(name=username)
            user_type = input(f"Bem vindo {self.user.name}! Como posso ajudá-lo? \n Cliente(C) \n Administrador(A) \n Sair(E) \n Selecionado:")
            if user_type == "C":
                self.client_intention()
            elif user_type == "A":
                is_admin = self.valid_admin()
                if is_admin:
                    self.user.permission = True
                    self.admin_intention()
            elif user_type == "E":
                self.is_on = False
            else:
                print("Digite uma opção válida!")




