import emoji

try: 
    print(emoji.emojize(input("Insert emoji string:")))
except (IndexError, ValueError):
    print("Entry invalid!")