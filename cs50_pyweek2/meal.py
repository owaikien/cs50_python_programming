def main():
    time = input("What time is it (in this format: x.x):")
    hours, minutes = time.split(":")
    timeCheck = float(convert(hours, minutes))

    if 7.0 <= timeCheck <= 8.0:
        print ("Breakfast time")
    elif 12.0 <= timeCheck <= 13.0:
        print ("Lunch time")
    elif 18.0 <= timeCheck <= 19.0:
        print ("Dinner time")

def convert(hours, minutes):
    hours = float(hours)
    minutes = round(float(minutes)/60, 2)
    return float(hours) + float(minutes)

main()