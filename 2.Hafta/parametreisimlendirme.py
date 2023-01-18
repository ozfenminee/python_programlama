def topla(*toplanacak, fazladan=0):
    toplam = 0
    for deger in toplanacak:
        toplam += deger + fazladan
    return toplam
print(topla(2, 8, 9, 16, 7.2, fazladan=3), file="a.txt")