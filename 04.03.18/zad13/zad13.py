f = lambda x: x * f(x-1) if x != 0 else 1
print(f(200))
