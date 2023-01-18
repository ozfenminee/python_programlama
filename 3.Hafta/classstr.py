class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __str__(self):
        return "Yazdırdığımız : " + self.metin
nesne = sinif("nnn")
print(nesne)