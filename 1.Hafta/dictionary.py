sozluk = {
  "marka": "dhhjfjhf",
  "model": "dnmjdjd",
  "yil": 1963
}
print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])
sozluk["renk"] = "pembe"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "siyah"
print(sozluk)
print(sozluk.keys())
print(sozluk.values())
for i in sozluk.keys():
    print(i, ":", sozluk[i])