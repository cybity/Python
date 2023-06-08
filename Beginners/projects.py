# Search Engine

text = input()
word = input()

def search(text, word):
    if word in text:
        return "Word Found"
    else:
        return "Word Not Found"
    
print(search(text,word))
