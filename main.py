print("Hello, world!")


def sum_squares(x):
    s = 0
    for xi in x:
        s += xi**2
    return s


def sum_cubes(x):
    s = 0
    for xi in x:
        s += xi**3
    return s


z = [1, 2, 0, 3]
r = sum_squares(z)
assert r == 14


a = [1, 2, 3]
expected_result = 36
sc = sum_cubes(a)
print(sc)
assert expected_result == sc
