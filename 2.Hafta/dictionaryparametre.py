def islem(**birim):
  print("birimin tipi :", type(birim))
  print("Birim İsmi : " + birim["isim"])
  print("Birim Tipi : ", birim["tip"])
  print("Birim Yılı : ", birim["yil"])
islem(ad="muğla", tip="lise", yil=2015)