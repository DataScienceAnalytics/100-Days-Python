
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO: 1. Print report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# TODO: 2. Check if there are sufficient resources
def check_resources(item_name):
    resources_sufficient = True
    item_ingredient_dict = MENU[item_name]['ingredients']
    for key, value in item_ingredient_dict.items():
        if resources[key] < value:
            resources_sufficient = False
            print('Sorry. Not enough '+ key)
            break
    return resources_sufficient

# TODO: 3. Process coins (check + charge if sufficient)

def check_coin(item_name):
    item_cost = MENU[item_name]['cost']

    if total_coin_inserted < item_cost:
        return False
    else:
        return True

# TODO: 4. Return the change based on the cost of the drink or showing not enough coin
def calculate_change(item_name):
    change = total_coin_inserted - MENU[item_name]['cost']
    return change

# TODO: 5 Add coin and deduce resouces
def receive_coint(item_name):
    resources['money'] += MENU[item_name]['cost']

def deduce_resources(item_name):
    item_ingredient_dict = MENU[item_name]['ingredients']
    for key, value in item_ingredient_dict.items():
        resources[key] -= value

# TODO: 6 Final Program
continue_or_not = 1

while continue_or_not == 1:
    item = input('What would you like? (espresso/latte/cappuccino): ')
    if item == 'report':
        print_report()

    elif item == 'off':
        continue_or_not = 0
        break

    else:
        print("Please insert coins.")
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))
        total_coin_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

        if check_coin(item) == True:
            if check_resources(item) == True:
                receive_coint(item)
                deduce_resources(item)
                change_amount = calculate_change(item)
                print('Here is your '+item + '. Enjoy!')
                print('Your change is: $'+str(round(change_amount,2)))
        else:
            print("Sorry that's not enough money. Money refunded!")
            
