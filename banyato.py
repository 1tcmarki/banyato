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

"""
3. feladat
Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint
a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre!
A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg! 
"""
def megszamolas(m):
    db=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                db+=1
    return db

def atlagolas(m):
    osszeg=0
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
                osszeg+=elem
    return osszeg/darab


felszin=megszamolas(melysegek)
atlagos_melyseg=0
print("3. feladat")
print(f"A tó felszíne: {megszamolas(melysegek*1)} m2, átlagos mélysége: {atlagolas(melysegek)/10:0.2f} m")

"""
4. feladat
Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ
a képernyőn! A legmélyebb pont koordinátáit a mintának megfelelően (sor; oszlop)
formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja
jelenjen meg!
"""
print("4. feladat")
def max_kivalasztas(m):
    max_sor=0
    max_oszlop=0
    for i in range(1,len(m)):
        for j in range(len(m[i])):
            if m[max_sor][max_oszlop]<m[i][j]:
                max_sor=i
                max_oszlop=j
    return max_sor , max_oszlop

max_kivalasztas(melysegek)


max_s, max_o, = max_kivalasztas(melysegek)
print(f"A tó legnagyobb mélysége: {melysegek[max_s][max_o]} dm")
def legmelyebb_pontok_koordinatai(m,max):
    for sor_index,sor in enumerate(m):
        for oszlop_index,elem in enumerate(sor):
            if elem==max:
                print(f"({sor_index+1} ; {oszlop_index+1})",end=" ")
    print()


legmelyebb_pontok_koordinatai(melysegek, melysegek[max_s][max_o])


"""
5. feladat
Milyen hosszú a tó partvonala, vagyis az ábrán a szürkével jelölt részt határoló vastag fekete
vonal hossza? A partvonalhoz vegye hozzá a tóban lévő szigetek kerületét is! Írassa ki
az eredményt a mintának megfelelően a képernyőre! (A megoldás során felhasználhatja,
hogy a táblázat első és utolsó sorában és oszlopában minden adat 0.) 
"""
print("5. feladat")
def partvonal_hossza(m):
    hossz=0
    for i in range(1,len(m)-1):
        for j in range(1,len(m[i])-1):
            if m[i][j]>0:
            

                if m[i-1][j]==0:
                    hossz+=1
                if m[i+1][j]==0:
                    hossz+=1
                if m[i][j-1]==0:
                    hossz+=1
                if m[i][j-1]==0:
                    hossz+=1
        

    return hossz
print(f"A tó partvonala {partvonal_hossza(melysegek)} m hosszú")

"""
6. feladat
Kérje be a felhasználótól egy oszlop azonosítóját, és szemléltesse a diagram.txt
szöveges állományban „sávdiagramon” a tó mélységét az adott oszlopban a következő
módon! A sor elején jelenjen meg a mérési adat sorának azonosítója pontosan két
számjeggyel, majd tegyen egymás mellé annyi csillagot (*), ahány méter az adott hely
"""
print("6. feladat")
be_oszlop=int(input("A vizsgált szelvény oszlopának azonosítója= ") or "6" )-1
with open("diagram.txt","w",encoding="utf-8") as fout:
    for sor_index , sor in enumerate(melysegek):
        print(f"{sor_index+1:2d}","*"*sor[be_oszlop], file=fout)