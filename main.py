from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_king = CoffeeMaker()
menu_king = Menu()
money_king = MoneyMachine()
loop = True

while loop:
    option = menu_king.get_items()
    usr_input = input(f"What drink would you like {option} \t").lower()
    if usr_input == 'report':
        coffee_king.report()
        money_king.report()
    elif usr_input == 'off':
        loop = False
    else:
        drink = menu_king.find_drink(usr_input)
        loop = coffee_king.is_resource_sufficient(drink)
        if loop:

            money_king.make_payment(drink.cost)
            coffee_king.make_coffee(drink)
        else:
            exit()







