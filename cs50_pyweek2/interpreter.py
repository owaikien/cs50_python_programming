import math

def main():
    Expression = input("expression:")
    x, y, z, = Expression.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(add(x, z))
    elif y == "-":
        print(sub(x, z))
    elif y == "*":
        print(multi(x,z))
    elif y == "/":
        print(div(x,z))

    
def add(x, z):
    return x+zß
def sub(x, z):
    return x-z
def multi(x, z):
    return x*z
def div(x, z):
    return x/z

