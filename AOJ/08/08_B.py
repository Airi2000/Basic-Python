while True:
    x = input()
    if x == "0":
        break
    sum = 0
    for i in x:
        sum += int(i)
    print(sum)
