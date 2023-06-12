def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)

def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

print((lambda x: x**2 + 5*x +4) (-4))
