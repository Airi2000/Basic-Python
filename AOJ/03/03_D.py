x, y, z = map(int, input().split())
n = 0
for i in range(x, y+1):
    if z % i == 0:
        n = n+1
print(n)
