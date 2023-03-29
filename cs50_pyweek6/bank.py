def main():
    greet = (input("Greeting: ")).lower().strip()
    print(f"${value(greet)}")


def value(greeting):
    if str(greeting).lower().strip().startswith("hello"):
        return 0
    elif str(greeting).lower().strip().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()