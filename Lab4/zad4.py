class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed,"Złotych")
chleb = NaZakupy("Chleb",21,"szt",3)
print(chleb.ile_kosztuje())