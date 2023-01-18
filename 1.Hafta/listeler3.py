liste = ["Mine", "Çağla", "Şennaz"]
liste.reverse()
print(liste)
liste.sort()
print(liste)
def fonksiyon(m):
  return abs(m - 50)
sayilistesi = [12,36,98,152]
sayilistesi.sort(key=fonksiyon)
print(sayilistesi)