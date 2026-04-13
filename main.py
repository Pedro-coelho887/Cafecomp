from coffee_machine import CoffeeMachine

def main():
    machine = CoffeeMachine()
    while machine.is_on:
        """TO DO: Funcionamento da Máquina"""
        user_option = input(" (B) Comprar Bebida Quente \n (C) Comprar Café \n (A) Modo administrador \n (E) Sair \n")
        
        if user_option == "E":
            # Desliga a Máquina
            machine.is_on = False

        elif user_option == "B":
            # Processo de comprar Bebida avulsa
            drink = machine.select_hot_drink()
            if drink != "E":
                payment = machine.financial_transaction(drink)
                if payment:
                    machine.give_hot_drink(drink)
        
        elif user_option == "A":
            # Administrador
            valid_admin = machine.valid_admin()
            if valid_admin:
                machine.admin_options()
                machine.fill_ingredients()
                machine.withdraw_money()
                machine.new_product()

        elif user_option == "B":
            payment = machine.financial_transaction(drink)
            if payment:
                drink = machine.dose_drink()

                

if __name__ == "__main__":
    main()