class DataStorage:
    def __init__(self):
        self.candrinks_stock = {}
        self.coffee_stock = {}

    def read_candrinks_stock(self,filepath):
        """Lê o arquivo de estoque e transforma em um dicionário"""
        result = {}
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


    def update_candrinks_stock(self,user,accountBalance,selling = True):
        """Atualiza a base de transações e o estoque"""
        if selling:
            self.update_transaction("data/transactions.txt",user,accountBalance)
        print(self.candrinks_stock)
        with open("data/candrinks_stock.txt","w",encoding="utf-8") as f:
            f.write("Codigo Estoque Preco Descricao\n")

            for code,info in self.candrinks_stock.items():
                line = f"{code}     {info["Quantidade"]}     {info["Preço"]}     {info["Descrição"]}\n"
                f.write(line)



        
           