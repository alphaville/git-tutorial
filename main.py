print("Hello, world!")


def sum_squares(x):
    s = 0
    for xi in x:
        s += x**2
    return s


z = [1, 2, 3, 4]
r = sum_squares(z)
print(z)
