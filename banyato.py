"""
1. feladat
Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
meg a következő feladatokat! 
"""
melysegek=[]

with open("melyseg.txt","r",encoding="utf-8") as fin:
    fin.readline()
    fin.readline()
    for sor in fin:
        seged_lista=list(map(int,sor.strip().split()))
        melysegek.append(seged_lista)
# print(melysegek)

from colorama import Fore , Back

for melyseg_sor in melysegek:
   for melyseg in melyseg_sor:
       if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}",end=" ")
       else:
            print(f"{Back.RESET}{Fore.RESET}{melyseg:2d}",end=" ")
   
   print() 

"""
2. feladat
Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen
mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!) 
"""
print("2. feladat")
be_sor=int(input("A mérés sorának azonosítója= (12) ") or "12")
be_oszlop=int(input("A mérés oszlopának azonosítója= (6) ") or "6")
print(f"A mért mélység az adott helyen {melysegek[be_sor-1][be_oszlop-1]} dm")