def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

def test(funcy, arg):
    return(funcy(funcy(arg)))

def mult(x):
    return x * x

print(test(mult,2))

# Pure Function 
def pure_function(x,y):
    temp = x + 2*y
    return temp/(2*x+y)
# Impure Function 

some_list = []
def impure(arg):
    some_list.append

def func(x):
    y = x**2
    z = x+y
    return z