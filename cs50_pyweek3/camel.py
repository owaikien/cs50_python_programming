text = input("camelCase:")

for word in text:
    if word.isupper():
        newText = "_" + word.lower()
        word = newText
    print(word, end="")
