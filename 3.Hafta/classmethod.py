class sinif:
    a = 7
    b = "mcs"
    c = [2,3,6]
    def yazdir(self):
        d = 200
        print(d, self.a)
    def yazdir2(self, t):
        self.yazdir()
        print(t)
nesne = sinif()
nesne.yazdir()
nesne.yazdir2("mnmnmn")