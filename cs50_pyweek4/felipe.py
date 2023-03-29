menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

totalPrice = 0

while True:
    try:
        order = input("Item: ")
        order = order.title()
        totalPrice += menu[order]
        print(f"Total: ${totalPrice:.2f}")

    except EOFError:
        print("\n")
        break
    except KeyError:
        pass
