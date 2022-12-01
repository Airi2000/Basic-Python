n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i != n-1:
        print(a[n-1-i], end=" ")
    else:
        print(a[n-1-i])
