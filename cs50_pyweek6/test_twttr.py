def main():
    text = input("Word: ")
    word = shorten(text)
    print (word)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    shortened = []
    for v in word:
        if v.casefold() not in vowels:
            shortened.append(v)
    output = str("".join(shortened))
    return output

if __name__ == "__main__":
    main()