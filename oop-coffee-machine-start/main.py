from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# print(money_machine.make_payment(1.5))

input_str = input('What would you like? (espresso/latte/cappuccino): ')

while input_str != 'off':
    if input_str == 'report':
        coffee_maker.report()
        money_machine.report()
        input_str = input('What would you like? (espresso/latte/cappuccino): ')

    elif input_str in ['espresso','latte','cappuccino']:
        item_select = menu.find_drink(input_str)
        if coffee_maker.is_resource_sufficient(item_select):
            if money_machine.make_payment(item_select.cost):
                coffee_maker.make_coffee(item_select)
                input_str = input('What would you like? (espresso/latte/cappuccino): ')
            else:
                input_str = input('What would you like? (espresso/latte/cappuccino): ')
        else:
            input_str = input('What would you like? (espresso/latte/cappuccino): ')
    else:
        print('wrong input')
        input_str = input('What would you like? (espresso/latte/cappuccino): ')

else:
    print('turn off')


# Solution 2 - Set a flag is_on = True outside of the loop. Put input inside the while loop. Way more optimized without
# having multiple input inside the loop
