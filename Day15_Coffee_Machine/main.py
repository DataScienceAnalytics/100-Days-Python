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
}

money = 0


def report():
    for key in resources:
        if key in ['water','milk']:
            print(key + ': ' + str(resources[key])+'ml')
        elif key in ['coffee']:
            print(key + ': ' + str(resources[key])+'g')
    print("Money: $"+str(money))

def sum_money():
    print('Please insert coins.')
    quarters = int(input('how many quarters?:'))
    dimes = int(input('how many dimes?:'))
    nickles = int(input('how many nickles?:'))
    pennies = int(input('how many pennies?:'))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

def resource_enough(drink):
    enough = True;
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > resources[key]:
            enough = False
    return enough


def deduct_resource(drink):
    for key in MENU[drink]["ingredients"]:
        resources[key] = resources[key] - MENU[drink]["ingredients"][key]


input_str = input('What would you like? (espresso/latte/cappuccino): ')

while input_str != 'off':
    if input_str == 'report':
        report()
        input_str = input('What would you like? (espresso/latte/cappuccino): ')

    elif input_str in ['espresso','latte','cappuccino']:

        total_coin = sum_money()
        if MENU[input_str]["cost"] <= total_coin:  # check coin
            if resource_enough(input_str):  # check resource
                # add money
                money += MENU[input_str]["cost"]
                # deduct resources
                deduct_resource(input_str)
                print("Order success!")
                # print change
                change = total_coin-MENU[input_str]["cost"]
                print("here is your change of $"+str(round(change,2)))
                input_str = input('What would you like? (espresso/latte/cappuccino): ')
            else:
                print("Insufficient Resources")
                input_str = input('What would you like? (espresso/latte/cappuccino): ')

        else:
            print("Insufficient Coins")
            input_str = input('What would you like? (espresso/latte/cappuccino): ')

    else:
        print('wrong input')
        input_str = input('What would you like? (espresso/latte/cappuccino): ')

else:
    print('turn off')

