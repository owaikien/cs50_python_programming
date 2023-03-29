import string
# GAVE UP

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

inte = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_valid(s):
    if 2 <= len(s) <= 6:
        return True
    if s[0:1] in string.ascii_lowercase or s[0:1].upper() in string.ascii_uppercase:
        return True
    if s[0] in inte or s[-1] in inte:
        return True
    

main()