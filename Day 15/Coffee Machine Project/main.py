MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
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
    "profit": 0
}
to_continue = True

while to_continue:
    print("Hello! Welcome to Rucha's Cafe!")
    kind = input("What would you like today? (espresso(e)/ cappucino(c)/ latte(l)): ").lower()

    def check():
        if MENU[kind]["ingredients"]["water"] <= resources["water"] and MENU[kind]["ingredients"]["milk"] <= resources["milk"] and MENU[kind]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            return False

    def make():
        resources["water"] -= MENU[kind]["ingredients"]["water"]
        resources["milk"] -= MENU[kind]["ingredients"]["milk"]
        resources["coffee"] -= MENU[kind]["ingredients"]["coffee"]
        resources["profit"] += total

    if kind == "report":
        print(resources)
    elif kind == "off":
        print("Goodbye.")
        to_continue = False
    elif kind == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    elif kind == "e" or "c" or "l":
        if check():
            print(f"The total will be: ${MENU[kind]["cost"]}")
            print("Please input coins:")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))

            total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            if total == MENU[kind]["cost"]:
                make()
                print("ENJOY!")
                input("Press Enter.")
            elif total > MENU[kind]["cost"]:
                change = round(total - MENU[kind]["cost"], 2)
                print(f"Here is the change of ${change}")
                total -= change
                make()
                print("ENJOY!")
                input("Press Enter.")
            else:
                print("Sorry that's not enough money. Money Refunded.")
                input("Press Enter.")

        else:
            print("Not enough resources. Please refill")


