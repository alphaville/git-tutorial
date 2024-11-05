print("Hello, world!")


def sum_squares(x):
    s = 0
    for xi in x:
        s += xi**2
    return s


z = [1, 2, 0, 3]
r = sum_squares(z)
assert r == 14
