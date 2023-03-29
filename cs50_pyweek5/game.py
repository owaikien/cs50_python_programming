import random


while True:
    try:
        n = int(input("Level:"))
        number = random.randint(1, n)
        while True:
            guess = int(input("Guess:"))
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
