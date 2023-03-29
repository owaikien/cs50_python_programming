fruit = input("Please enter a fruit:")

fda = {"apple":130, "avacado":50, "banana":110, "cantaloupe":50, "grapefruit":60, "grapes":90}
fruit = fruit.lower()
if fruit in fda.keys():
    print(f'Calories: {fda[fruit]}')
else:
    print("Error!")