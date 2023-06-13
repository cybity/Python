def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap

def print_text():
    print("Frey0xD")

decorated = decor(print_text)

@decor
def print_text():
    print("Hello Hacker!")
print_text()

decorated()