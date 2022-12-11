import itertools

while True:
    n, x = map(int, input().split())
    a = 0
    if n == 0 and x == 0:
        break
    m = range(1, n+1)
    for i in list(itertools.combinations(m, 3)):
        s = sum(i)
        if s == x:
            a += 1
    print(a)
