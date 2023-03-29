items = {}
while True:
    try:
        item = input("item:").upper().strip()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        print("\n")
        sorted_dict = dict(sorted(list(items.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep= " ")
        break
    except KeyError:
        pass

