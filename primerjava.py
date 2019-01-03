import random

#import ilp as ILP
import GRASP as GRASP
import uvoz as uv
import matrike as m


# funkcije

# GRASP.dolzina_poti(g,pot)
# GRASP.local_search(g,k,iter, metoda)

# uv.TSP(N, max)
# uv.preberi_matriko(datoteka,velikost, k = 7) #za swiss42
# uv.geo_razdalje(datoteka, velikost,k = 7) #za ulysses22
# uv.razdalje(datoteka, velikost,k = 6) #za berlin52 in kroA100


# primeri od skupine 7 
ulysses22 = uv.geo_razdalje("ulysses22.tsp",22)
berlin52 = uv.razdalje("berlin52.tsp",52)
kroA100 = uv.razdalje("kroA100.tsp",100)

# primeri
swiss42 = uv.preberi_matriko("swiss42.tsp",42)

kroD100 = uv.razdalje("kroD100.tsp",100)
pr76 = uv.razdalje("pr76.tsp",76)


#funkcija vrne povprečje cen pri določenemu številu ponovitev in najboljšo pot
def povprecje(ponovitve,g,k,iter, metoda):
    min_pot = GRASP.local_search(g,k,iter, metoda)
    min_resitev = min_pot[0]
    vsota = min_resitev
    for i in range (ponovitve-1):
        resitev = GRASP.local_search(g,k,iter, metoda)
        l = resitev[0]
        vsota += l
        if l < min_resitev:
            min_resitev = l
            min_pot = resitev
            
    povprecje = vsota / ponovitve
    return (povprecje, min_resitev)

# primerjava rezultatov za različne vrednosti parametra alfa

# swiss42 velikosti 42x42
# ponovitve = 10, iter = 100

# dva_opt

## povprecje(20,swiss42,5,100,"dva_opt") # best = 1273
## povprecje(20,swiss42,10,100,"dva_opt") # best = 1326
## povprecje(20,swiss42,15,100,"dva_opt") # best = 1431
## povprecje(20,swiss42,30,100,"dva_opt") # best = 1539

# tri_opt

# iter = 100

## povprecje(10,swiss42,5,100,"tri_opt") # best = 
## povprecje(10,swiss42,10,100,"tri_opt") # best = 
## povprecje(10,swiss42,15,100,"tri_opt") # best = 
## povprecje(10,swiss42,30,100,"tri_opt") # best =


##alfa_3 = povprecje(10,ulysses22,3,10,"dva_opt")
##alfa_5 = povprecje(10,ulysses22,5,10,"dva_opt")
##alfa_7 = povprecje(10,ulysses22,7,10,"dva_opt")
##alfa_10 = povprecje(10,ulysses22,10,10,"dva_opt")
##alfa_13 = povprecje(10,ulysses22,13,10,"dva_opt")
##alfa_17 = povprecje(10,kroA100,150,10,"dva_opt")
##
##print(alfa_3)
##print(alfa_5)
##print(alfa_7)
##print(alfa_10)
##print(alfa_13)
##print(alfa_17)

#swiss42
##(1318.3, 1273)
##(1342.75, 1274)
##(1373.2, 1297)
##(1454.25, 1334)
##(1523.2, 1376)
##(1621.7, 1437)

#ulysses22







# primer matrike




