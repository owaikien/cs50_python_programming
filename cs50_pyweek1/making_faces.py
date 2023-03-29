def convert(input):
    input = input.replace(":)", "🙂")
    input = input.replace(":(", "🙁")
    return input

def main():
    s = input()
    print(convert(s))
    
main()

