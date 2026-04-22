class DataStorage:
    def __init__(self):
        self.candrinks_stock = {}
        self.ingredients_stock = {}
        self.admins = {}

    def read_candrinks_stock(self,filepath):
        """Lê o arquivo de estoque e transforma em um dicionário"""
        with open(filepath) as f:
            products = f.readlines()

        for product in products[1:]:
            parts = product.strip().split()
            code = parts[0]
            quantity = int(parts[1])
            price = float(parts[2])
            description = " ".join(parts[3:])
            self.candrinks_stock[code] = {"Quantidade":quantity,
                            "Preço": price,
                            "Descrição":description}

    def read_ingredients_stock(self,filepath):
        """Lê o Arquivo de Estoque de ingredientes"""
        with open(filepath) as f:
            ingredients = f.readlines()

        for ingredient in ingredients[1:]:
            parts = ingredient.strip().split()
            description = parts[0]
            quantity = int(parts[1])
            self.ingredients_stock[description] = int(quantity)     
    
    def update_transaction(self,filepath,user,accountBalance):
        """Atualiza o histórico de transações"""
        transaction = {
            "name": user.name,
            "code": user.drink.code,
            "price": user.drink.price,
            "method":user.payment_method,
            "balance": accountBalance
        }
        formated_transaction = f"{transaction['name']}    {transaction['code']}    {transaction['price']}    {transaction["method"]}      {transaction['balance']}\n"
        with open(filepath,"a",encoding="utf-8") as f:
            f.write(formated_transaction)


    def update_candrinks_stock(self,user=None,accountBalance=None,selling = True):
        """Atualiza a base de transações e o estoque de bebidas em lata"""
        if selling:
            self.update_transaction("data/transactions.txt",user,accountBalance)

        with open("data/candrinks_stock.txt","w",encoding="utf-8") as f:
            f.write("Codigo Estoque Preco Descricao\n")

            for code,info in self.candrinks_stock.items():
                line = f"{code}     {info["Quantidade"]}     {info["Preço"]}     {info["Descrição"]}\n"
                f.write(line)

    def update_ingredients_stock(self,user = None,accountBalance=None,selling=True):
        """Atualiza a base de transações e estoque de ingredientes"""
        if selling:
            self.update_transaction("data/transactions.txt",user,accountBalance)

        with open("data/ingredients_stock.txt","w",encoding="utf-8") as f:
            f.write("Ingrediente   Quantidade\n")

            for type,quantity in self.ingredients_stock.items():
                line = f"{type}   {quantity} \n"
                f.write(line)

    def get_admins(self,filepath):
        """Guarda os Admins e sua senha"""
        with open(filepath) as f:
            admins = f.readlines()

        for admin in admins[1:]:
            parts = admin.strip().split()
            admin_name = parts[0]
            admin_password = parts[1]
            self.admins[admin_name] = admin_password

    def show_stats(self,filepath):
        pass



        
           