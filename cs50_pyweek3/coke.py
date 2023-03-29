print("Amount Due: 50")
changeOwned = 50
while changeOwned > 0:
    coin = int(input(f"Insert only 25, 10 or 5 cents!"))
    if coin < 0:
        print("Amount due: 50")
    elif coin == 5 or coin == 10 or coin == 25:
        changeOwned -= coin
        if changeOwned < 0:
            break
        print("Amount Due:" + str(changeOwned))
    else:
        print("50")

print("Change owned:" + str(abs(changeOwned)))