suit = ["S", "H", "C", "D"]
n = int(input())
c = [list(input().split()) for _ in range(n)]
cards = [[False for i in range(13)] for j in range(4)]
for i in range(n):
    cards[suit.index(c[i][0])][int(c[i][1])-1] = True
for i in range(4):
    for j in range(13):
        if not cards[i][j]:
            print(suit[i], j+1)
