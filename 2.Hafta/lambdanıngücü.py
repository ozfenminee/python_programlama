
def fonksiyonum(m):
  return lambda a: a * m
katini_al = fonksiyonum(7)
print(katini_al(8))
kati = fonksiyonum(8)
print(kati(8))