def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def product(a, b):
    return a*b


def quot(a, b):
    return a//b


while 1:
    a, op, b = input().split()
    a, b = int(a), int(b)
    if op == "+":
        print(sum(a, b))
    if op == "-":
        print(diff(a, b))
    if op == "*":
        print(product(a, b))
    if op == "/":
        print(quot(a, b))
    if op == "?":
        break
