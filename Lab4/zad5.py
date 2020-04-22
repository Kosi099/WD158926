class Ciagi_Arytm:
    def __init__(self,ciag):
        self.ciag = ciag
    def wyswietl_dane(self):
        print(self.ciag)
    def pobierz_elementy(self):
        self.ciag1 = []
        for i in range(0,int(self.ilosc_elementow)):
            self.a = input("Podaj element = ")
            self.ciag1.append(self.a)
    def pobierz_parametry(self):
        self.pierw_wart = input("Podaj pierwsza wartosc = ")
        self.roznica = input("Podaj roznice = ")
        self.ilosc_elementow = input("Ile jest elementow = ")
    def policz_sume(self):
        self.suma = 0
        for i in range(0,int(self.ilosc_elementow)):
            self.suma+=int(self.ciag1[i])
        return self.suma

ciag = [1,2,3,4,5]
Ciagi = Ciagi_Arytm(ciag)
Ciagi.pobierz_parametry()
Ciagi.pobierz_elementy()
print(Ciagi.policz_sume())