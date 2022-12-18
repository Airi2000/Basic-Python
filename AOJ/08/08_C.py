import sys
lines = sys.stdin.read()
low_lines = lines.lower()
sam = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    number = 0
    for j in low_lines:
        if j == sam[i]:
            number += 1
    print(f"{sam[i]} : {number}")
