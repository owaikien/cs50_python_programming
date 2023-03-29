import random

def main():
    eqn = 10
    chances = 3
    score = 0
    lvl = get_level()
    while eqn != 0:
        if chances == 3:
            x, y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} ="))
            answer = x + y
            if user_answer == answer:
                score += 1
                eqn -= 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print(f"{x} + {y} = {answer}")
            chances = 3
            eqn -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    elif level == 3:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return X, Y

main()