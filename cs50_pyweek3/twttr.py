input = str(input("Input:"))

a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newText = ""

for i in range(len(input)):
    if input[i] not in a:
        newText += input[i]

text = newText
print(text)