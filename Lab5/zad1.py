class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def wyswietl_nazwa(self):
        print(self.rodzaj)
class Ubrania(Material):
    def wyswietl_dane(self):
        print(self)
class Sweter(Ubrania):
    def wyswietl_dane(self):
        print(self)

