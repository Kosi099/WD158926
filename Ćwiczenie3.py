import random
#Zadanie 1
A = [1/x for x in range(1,11)]
B = [2**x for x in range (11)]
C = [x for x in B if x % 4 == 0]
#Zadanie 2
lista1 = [random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)]
lista2 = [random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)]
lista3 = [random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)]
lista4 = [random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)]
macierz = [lista1,lista2,lista3,lista4]
przekatna = [lista1[0],lista2[1],lista3[2],lista4[3]]
#Zadanie 3
skroty = {'Chleb':'sztuki','Ziemniaki':'kg','Papier_Toaletowy':'sztuki'}
lista = []
if skroty['Chleb']=="sztuki":
    lista.append("Chleb")
if skroty['Ziemniaki']=="sztuki":
    lista.append("Ziemniaki")
if skroty['Papier_Toaletowy']=="sztuki":
    lista.append("Papier_Toaletowy")
print(lista)