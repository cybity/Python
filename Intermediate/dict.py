# List
x = ['hi','x0x0','welcome']
print(x[2])
age = {
    "David":32,
    "frey":21,
    "ayush":35
}
print(age["David"])
# Note Only immutable objects can be used as keys to dict.

# bad_dict = {
#     [1,2,3] : "one two three",
# }
car = {
    'brand' : "bmw",
    'year' : 2023,
    'owner' : 'frey',
    'color' : 'red'   
}
a = input("car details:- ")
print(car[a])
# Dict Function
print('year' in car)
print('elon' not in car)

space = {
    1 : "NASA",
    "Asteroid" : "433 Eros",
    True : False,
    "missions": [1958,1961,1960],
    "Black hole" : "Messier 87",
    "Cosmos" : "ALL",
    "Nebula" : "NGC 7635",   
}
print(space.get("missions"))
print(space.get(7,42))
print(space.get(12345, "not found"))