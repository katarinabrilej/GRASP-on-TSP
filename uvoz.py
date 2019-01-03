import random
import numpy as np
import os
import math


# N je stevilo mest (torej dimenzija incidencne matrike)
# max_pot je največja razdalja / cena poti
def TSP(N, max_pot, min_pot = 1):
    " funkcija vrne naključno matriko cen povezav, ki predstavlja problem potujočega trgovca"
    a = np.random.randint(min_pot, max_pot, size= (N,N))
    m = np.tril(a) + np.tril(a, -1).T
    for i in range(N):
        m[i][i] = 0
    return m

# funkcija, ki prebere TSP, če je zapisan kot txt matrika in naredi matriko
def preberi_matriko(datoteka,velikost, k = 7):
    pot = os.path.join(os.getcwd() + "/testni_primeri", datoteka)
    with open(pot, 'r') as f:
        vsebina = f.readlines()
        vsebina = vsebina[k:(k+velikost)]
    matrika = [[int(num) for num in line.strip().split()] for line in vsebina]
    return matrika

# primer za tsp swiss42 velikoti 42x42        
swiss42 = preberi_matriko("swiss42.tsp",42)

#funkcija iz datoteke prebere koordinate mest, te so lahko v decimalnem zapisu ali pa v stopinjah
def preberi_koordinate(datoteka,velikost,k):
    " funkcija sprejme datoteko v kateri je zapisan TSP problem in velikost ter vrne seznam mest oblike "
    " [mesto, x koordinata, y koordinata]"
    pot = os.path.join(os.getcwd() + "/testni_primeri", datoteka)
    with open(pot, 'r') as f:
        vsebina = f.readlines()
        vsebina = vsebina[k:(k+velikost)]
        mesta = []
        for vrstica in vsebina:
            vrstica.strip()
            ## print(vrstica.split())
            mesto, x, y = vrstica.split()
            mesta += [[int(mesto), float(x), float(y)]]
        return mesta


# v datoteki so v posamezni vrstici napisani zaporedna številka mesta ter koordinate
def geo_razdalje(datoteka, velikost,k = 7):
    " funkcija sprejme množico mest in njihove koordinate ter izračuna razdalje med mesti, ki jih "
    " zabeleži v matriko "
    mesta = preberi_koordinate(datoteka,velikost,k)
    matrika = np.zeros((velikost,velikost))

    pi = math.pi
    RRR = 6378.388

    for i in range(0,velikost):
        stopinje = int(mesta[i][1])
        minute = mesta[i][1] - stopinje
        radiani = pi * (stopinje + 5.0 * minute / 3.0) / 180.0
        mesta[i][1] = radiani

        stopinje = int(mesta[i][2])
        minute = mesta[i][2] - stopinje
        radiani = pi * (stopinje + 5.0 * minute / 3.0) / 180.0
        mesta[i][2] = radiani
             
    for i in range(0, velikost): 
        for j in range(i+1, velikost):
            q1 = math.cos(mesta[i][2] - mesta[j][2]) 
            q2 = math.cos(mesta[i][1] - mesta[j][1])
            q3 = math.cos(mesta[i][1] + mesta[j][1])
            matrika[i][j] = int(RRR * math.acos( 0.5*((1.0 + q1) * q2 - (1.0 - q1) * q3) ) + 1.0)
            matrika[j][i] = matrika[i][j]

    return matrika

# primer za tsp ulysses22 velikoti 22x22        
ulysses22 = geo_razdalje("ulysses22.tsp",22)


def razdalje(datoteka, velikost,k = 6):
    " funkcija sprejme množico mest in njihove koordinate ter izračuna evklidske razdalje med mesti, ki jih "
    " zabeleži v matriko "
    mesta = preberi_koordinate(datoteka,velikost,k)
    matrika = np.zeros((velikost,velikost))

    for i in range(0,velikost):
        for j in range(i+1, velikost):
            matrika[i][j] = ((mesta[i][1] - mesta[j][1])**2 + (mesta[i][2] - mesta[j][2])**2)**(1/2)
            matrika[j][i] = matrika[i][j]
            
    return matrika


# primer za tsp berlin52 velikoti 52x52        
berlin52 = razdalje("berlin52.tsp",52)

# primer za tsp kroA100 velikoti 100x100        
kroA100 = razdalje("kroA100.tsp",100)


