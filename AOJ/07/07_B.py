import itertools

while True:
    n, x = map(int, input().split())
    a = 0
    if n == 0 and x == 0:
        break
    m = range(1, n+1)
    c = (n*(n-1)*(n-2))//6
    com = list(itertools.combinations(m, 3))
    for i in range(c):
        s = sum(com[i])
        if s == x:
            a += 1
    print(a)
