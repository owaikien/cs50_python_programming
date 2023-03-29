months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            m, d, y = date.split("/")
        elif "," in date:
            md, y = date.split(", ")
            m, d = md.split(" ")
            m = (months.index(m)) +1
        if int(m) > 12 or int(d) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(y)}-{int(m):02}-{int(d):02}")
        break