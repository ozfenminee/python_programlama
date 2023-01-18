a = 5
while a < 12:
    a += 2
    if a == 8:
        continue
    if a == 12:
        break
    print(a)
else:
    print("a artık 12 ya da daha büyük")