def div_int(a, b):
    return a//b


def div_float(a, b):
    return a/b


def div_remainder(a, b):
    return a % b


a, b = map(int, input().split())
x, y, z = div_int(a, b), div_float(a, b), div_remainder(a, b)
print(x, z, "{:.8f}".format(y))
