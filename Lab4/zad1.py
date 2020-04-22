import random
plik = open("dane.txt","w")
lista=[]
for i in range(0,4):
    k=random.randint(1,100)
    while(k%4!=0):
       k=random.randint(1,100) 
    lista.append(k)
plik.writelines(str(lista))