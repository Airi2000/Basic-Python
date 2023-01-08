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

    def south_s(self):
        return self.number[1]


dice1 = Dice()
a, b, c, d, e, f = map(int, input().split())
dice1.setNumber(a, b, c, d, e, f)
dice2 = Dice()
a, b, c, d, e, f = map(int, input().split())
dice2.setNumber(a, b, c, d, e, f)
o = 0
for i in "SSSWSSSN":
    if dice1.south_s() == dice2.south_s():
        o = 1
        break
    dice2.roll(i)

for i in "EEEN":
    if dice1.top() == dice2.top():
        o += 1
        break
    dice2.roll(i)
if o != 2:
    print("No")
else:
    if dice1.number == dice2.number:
        print("Yes")
    else:
        print("No")
