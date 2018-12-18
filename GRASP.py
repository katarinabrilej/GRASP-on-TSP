import random
import numpy as np

# ustvarimo naključno matriko za TSP
def TSP(N, max_pot):
    a = np.random.randint(1, max_pot, size= (N,N))
    m = np.tril(a) + np.tril(a, -1).T
    for i in range(N):
        m[i][i] = 0
    return m

# primer matrike
K = [[ 0,  2,  1, 14,  2,  3, 20, 22, 22, 14],
       [ 2,  0,  3,  4, 22,  2,  5, 19,  4,  3],
       [ 1,  3,  0, 14, 22, 22, 21, 13,  2, 13],
       [14,  4, 14,  0, 11, 13, 10, 10, 24, 11],
       [ 2, 22, 22, 11,  0, 16,  3, 13,  4,  8],
       [ 3,  2, 22, 13, 16,  0, 13, 23, 22, 17],
       [20,  5, 21, 10,  3, 13,  0, 20, 10,  9],
       [22, 19, 13, 10, 13, 23, 20,  0,  4, 18],
       [22,  4,  2, 24,  4, 22, 10,  4,  0, 10],
       [14,  3, 13, 11,  8, 17,  9, 18, 10,  0]]

# funkcija, ki sprejme množico mest in njihove koordinate ter izračuna razdalje med mesti
# te razdalje zabeleži v matriko
def izracunaj_razdalje(datoteka):
    with open(datoteka, 'r') as f:
        vsebina = f.readlines()
        st_mest = len(vsebina)
        matrika = np.zeros(shape=(st_mest,st_mest))
        mesta = []
        for vrstica in vsebina:
            vrstica.strip()
            mesto, x, y = vrstica.split()
            mesta += [[int(mesto), float(x), float(y)]]
        for i in range(0,st_mest):
            for j in range(i+1, st_mest):
                matrika[i][j] = (mesta[j][2] - mesta[i][2])**2 + (mesta[j][1] - mesta[i][1])**2
                matrika[i][i] = 0
                matrika[j][i] = matrika[i][j] 
        return matrika
                
# ustvarimo slovar cen povezav
def slovar_cen(g):
    r = range(len(g))
    cena = {(i+1, j+1): g[i][j] for i in r for j in r}
    return cena

# vhodni podatki za algoritem
    # g je graf z vozlišči od 1 do n, podan v obliki incidenčne matrike
    # torej gij je razdalja(cena) med mestoma i in j
    # iter je število dovoljenih iteracij algoritma
    # k je število začetnih približkov, torej moč RCL

    # množica vseh rešitev CL je množica vseh Hamiltonovih ciklov v g
    # predstavimo jih kot zaporedja števil (l,1,v2,...,vn), vi je lahko od 2 do n
    # l je dolžina cikla (1,v2,...,vn) v grafu g 

def dolzina_poti(g,pot):
    n = len(g)
    slovar = slovar_cen(g)
    dolzina = 0
    for i in range(1,n):
            dolzina += slovar[(pot[i],pot[i+1])]
    return dolzina

# greedy randomized construction

# vsak začetni približek t = (l,1,v2,...,vn) iz RCL konstruiramo tako, da
# določimo v1 := 1 nato iterativno za i = 2,...,n za vi izberemo naključno
# med p % najbližjih vozlišč do vi-1, ki še niso v t
# take cikle t konstruiramo toliko časa, da RCL napolnimo
    
def greedy_construction(g,k):
    RCL = [0] * k
    slovar = slovar_cen(g)
    n = len(g)
    p = n // 5
    for j in range(0,k):
        t = [0] * (n+1)
        t[1] = 1
        mesta = [h for h in range(2,n+1)]
        for i in range(2,n+1):
            povezave = [(t[i-1],m) for m in mesta]
            cene = { key:value for key, value in slovar.items() if key in povezave }
            urejene_povezave = sorted(cene, key=cene.__getitem__)
            (_,vi) = random.choice(urejene_povezave[:p])
            t[i] = vi
            mesta.remove(vi)
        t[0] = dolzina_poti(g,t)
        RCL[j] = t
    return RCL
    
# local search

# elementi v RCL so urejeni po dolžini, primerjamo jih po l
# naključno izberemo t v RCL, toda z linearno padajočo verjetnostjo
# najverjetneje izbereme cikel na vrhu RCL - najkrajši
# okolico cikla t definiramo kot monožico vseh ciklov t' iz CL, ki jih dobimo
# iz t tako, da mu zamenjamo dve vozišči, torej naključno zamenjamo dve vozlišči t
# preverimo če smo s tem dobili krajši cikel
# če ja, t odstranimo iz RCL in dodamo t'
# ponavaljamo tolikokrat kot je predpisano (iter)


def local_search(g,k, iter):
    RCL = greedy_construction(g,k)
    n = len(g)
    slovar = slovar_cen(g)
    #urejen seznam začetnih približkov
    RCL.sort(key=lambda x: x[0])
    stevec = 0
    while stevec < iter:
        utezi = [i * 2/((k+1)*k) for i in range(k,0,-1)]
        indeks = np.random.choice(len(RCL), size = 1, p = utezi)
        t = RCL[indeks[0]]
        okolica = []
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                novi_t = [t[m] for m in range(0,n+1)]
                element_i = t[i]
                element_j = t[j]
                novi_t[i] = element_j 
                novi_t[j] = element_i
                
                novi_t[0] = dolzina_poti(g,novi_t)
                okolica.append(novi_t)
        okolica.sort(key=lambda x: x[0])
        if okolica[0][0] < t[0]:
                RCL.append(okolica[0])
                RCL.remove(t)   
        stevec += 1
        RCL.sort(key=lambda x: x[0])
    RCL.sort(key=lambda x: x[0])
    return RCL[0]

