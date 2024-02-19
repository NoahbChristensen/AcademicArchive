def change_calculator(change):
    change = change * 100
    dollars = change // 100
    change = change % 100
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    pennies = change
    print("Your change is: ", dollars, "dollars, ", quarters, "quarters, ", dimes, "dimes, ", nickels, "nickels, ", pennies, "pennies.")


def cashier():
    items = []
    prices = []
    total = 0
    while True:
        item = input("Enter the item name or 'done' to finish: ")
        if item == 'done':
            break
        price = float(input("Enter the price of the item: "))
        items.append(item)
        prices.append(price)
        total += price
    print("Your total is: ", total)
    payment = float(input("Enter the amount you're paying: "))
    change = payment - total
    return change_calculator(change)

def main():
    cashier()

if __name__ == "__main__":
    main()