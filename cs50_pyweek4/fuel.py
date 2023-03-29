while True:
    try:
        x, y = input("Fraction: ").split("/")
        if 0 <= int(x)/int(y) <= 0.1:
            print ("E")
        elif 0.9 <= int(x)/int(y) <= 1:
            print ("F")
        elif 0.1 < int(x)/int(y) < 0.9:
            print (str(round(int(x)/int(y)*100)) + "%")
        break
    except (ValueError, ZeroDivisionError):
        pass