import random
import numpy as np
import os
import math


# N je stevilo mest (torej dimenzija incidencne matrike)
# max_pot je največja razdalja / cena poti
def TSP(N, max_pot, min_pot = 1):
    " funkcija vrne naključno simetrično matriko razdalj med mesti/cen povezav,"
    " ki predstavlja problem potujočega trgovca"
    a = np.random.randint(min_pot, max_pot, size= (N,N))
    m = np.tril(a) + np.tril(a, -1).T
    for i in range(N):
        m[i][i] = 0
    return m

# v txt datoteki je TSP zapisan v obliki matrike
# kot argument podamo še velikost matrike
def preberi_matriko(datoteka,velikost, k = 7):
    " funkcija iz datoteke prebere podatke za TSP in vrne matriko razdalj "
    # vsi TSP so shranjeni v datoteki testni_primeri
    pot = os.path.join(os.getcwd() + "/testni_primeri", datoteka)
    with open(pot, 'r') as f:
        vsebina = f.readlines()
        # na začetku je k=7 vrstic z informacijami o podatkih 
        vsebina = vsebina[k:(k+velikost)]
    matrika = [[int(num) for num in line.strip().split()] for line in vsebina]
    return matrika

# primer za tsp swiss42 velikoti 42x42        
swiss42 = preberi_matriko("swiss42.tsp",42)

# v datoteki so podatki v vsaki vrstici oblike:
# zaporedna stevilka mesta x koordinata y koordinata
def preberi_koordinate(datoteka,velikost,k):
    " funkcija sprejme datoteko v kateri je zapisan TSP problem in velikost ter vrne seznam mest oblike "
    " [mesto, x koordinata, y koordinata]"
    pot = os.path.join(os.getcwd() + "/testni_primeri", datoteka)
    with open(pot, 'r') as f:
        vsebina = f.readlines()
        # na začetku je k vrstic z informacijami o podatkih
        vsebina = vsebina[k:(k+velikost)]        
        mesta = []
        for vrstica in vsebina:
            vrstica.strip()
            mesto, x, y = vrstica.split()
            mesta += [[int(mesto), float(x), float(y)]]
        return mesta


# v datoteki so podatki napisani v koordinatah tipa GEO
def geo_razdalje(datoteka, velikost,k = 7):
    " funkcija sprejme datoteko s podatki za TSP ter izračuna razdalje med mesti, ki jih zabeleži v matriko "
    # seznam mesta vsebuje podatke o koordinatah mest
    mesta = preberi_koordinate(datoteka,velikost,k)
    matrika = np.zeros((velikost,velikost))
    pi = math.pi
    RRR = 6378.388
    # podatke o koordinatah pretvorimo v radiane
    for i in range(0,velikost):
        # najprej za x koordinato
        stopinje = int(mesta[i][1])
        minute = mesta[i][1] - stopinje
        radiani = pi * (stopinje + 5.0 * minute / 3.0) / 180.0
        mesta[i][1] = radiani
        # nato še za y koordinato
        stopinje = int(mesta[i][2])
        minute = mesta[i][2] - stopinje
        radiani = pi * (stopinje + 5.0 * minute / 3.0) / 180.0
        mesta[i][2] = radiani
    # formula za izračun razdalje je napisana na strani TSPLIB, od koder so testni primeri        
    for i in range(0, velikost): 
        for j in range(i+1, velikost):
            q1 = math.cos(mesta[i][2] - mesta[j][2]) 
            q2 = math.cos(mesta[i][1] - mesta[j][1])
            q3 = math.cos(mesta[i][1] + mesta[j][1])
            matrika[i][j] = int(RRR * math.acos( 0.5*((1.0 + q1) * q2 - (1.0 - q1) * q3) ) + 1.0)
            matrika[j][i] = matrika[i][j]
    # vrnemo matriko razdalj med mesti
    return matrika

# primer za tsp ulysses22 velikoti 22x22        
ulysses22 = geo_razdalje("ulysses22.tsp",22)

# v datoteki so podatki napisani v koordinatah tipa EUC_2D
def razdalje(datoteka, velikost,k = 6):
    " funkcija sprejme datoteko s podatki za TSP ter izračuna razdalje med mesti, ki jih zabeleži v matriko "
    mesta = preberi_koordinate(datoteka,velikost,k)
    matrika = np.zeros((velikost,velikost))
    # zdaj računamo evklidsko razdaljo med mesti
    for i in range(0,velikost):
        for j in range(i+1, velikost):
            matrika[i][j] = ((mesta[i][1] - mesta[j][1])**2 + (mesta[i][2] - mesta[j][2])**2)**(1/2)
            matrika[j][i] = matrika[i][j]
    # vrnemo matriko razdalj med mesti        
    return matrika


# primer za tsp berlin52 velikoti 52x52        
berlin52 = razdalje("berlin52.tsp",52)

# primer za tsp kroA100 velikoti 100x100        
kroA100 = razdalje("kroA100.tsp",100)

# primer za tsp st70 velikoti 70x70        
st70 = razdalje("st70.tsp",70)
