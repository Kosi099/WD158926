class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x
    def __ge__(self):
        if self.x>=self.b:
            print("True")
    def __gt__(self):
        if self.x>self.b:
            print("True")
    def __le__(self):
        if self.x<=self.b:
            print("True")
    def __lt__(self):
        if self.x<self.b:
            print("True")