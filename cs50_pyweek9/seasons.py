from datetime import date
import inflect

def main():
    birthday = get_birthday()
    if birthday is None:
        return
    
    minutes = count_minutes(birthday)
    print(f"{minutes.capitalize()} minutes")

# Return value error if birthday is not in the format yyyy-mm-dd
def get_birthday():
    birthday = input("Birthday (yyyy-mm-dd): ")

    try:
        date.fromisoformat(birthday)
    except ValueError:
        print("Invalid date")
        return None
    
    return birthday

def count_minutes(birthday):
    today = date.today()
    birthday = date.fromisoformat(birthday)
    delta = today - birthday
    minutes = delta.days * 24 * 60

    p = inflect.engine()

    minutes = p.number_to_words(minutes)
    return minutes 

if __name__ == "__main__":
    main()