class Dice:

    def __init__(self):
        self.number = [0 for i in range(6)]

    def setNumber(self, a, b, c, d, e, f):
        self.number[0] = a
        self.number[1] = b
        self.number[2] = c
        self.number[3] = d
        self.number[4] = e
        self.number[5] = f

    def roll(self, dir):
        a = self.number[0]
        b = self.number[1]
        c = self.number[2]
        d = self.number[3]
        e = self.number[4]
        f = self.number[5]
        if dir == "E":
            self.setNumber(d, b, a, f, e, c)
        if dir == "N":
            self.setNumber(b, f, c, d, a, e)
        if dir == "S":
            self.setNumber(e, a, c, d, f, b)
        if dir == "W":
            self.setNumber(c, b, f, a, e, d)

    def top(self):
        return self.number[0]


dice = Dice()
a, b, c, d, e, f = map(int, input().split())
dice.setNumber(a, b, c, d, e, f)
d = input()
for i in d:
    dice.roll(i)
print(dice.top())
