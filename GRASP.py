import random
import numpy as np

# ustvarimo naključno matriko za TSP
def TSP(N, max_pot):
    a = np.random.randint(0, max_pot, size= (N,N))
    m = np.tril(a) + np.tril(a, -1).T
    for i in range(N):
        m[i][i] = 0
    return m
M = TSP(10,25)
MM = TSP(5,25)

#ustvarimo slovar cen povezav
def slovar_cen(matrika):
    r = range(len(matrika))
    dist = {(i+1, j+1): matrika[i][j] for i in r for j in r}
    return dist

#vhodni podatki za algoritem
    #g je graf z vozlišči od 1 do n, podan v obliki incidenčne matrike
    #torej gij je razdalja med mestoma i in j
    #iter je število dovoljenih iteracij algoritma
    #k je število začetnih približkov, torej moč RCL

    #množica vseh rešitev CL je množica vseh Hamiltonovih ciklov v g
    #predstavimo jih kot zaporedja števil (l,1,v2,...,vn), vi je lahko od 2 do n
    #l je dolžina cikla (1,v2,...,vn) v grafu g 

#greedy randomized construction
def grasp(g,k):
    zacetni_priblizki = [0] * k
    slovar = slovar_cen(g)
    n = len(g)
    st = n // 5
    for j in range(0,k):
        priblizek = [0] * (n+1)
        priblizek[1] = 1
        mesta = [h for h in range(2,n+1)]
        for i in range(2,n+1):
            povezave = [(priblizek[i-1],m) for m in mesta]
            cene = { key:value for key, value in slovar.items() if key in povezave }
            urejene_povezave = sorted(cene, key=cene.__getitem__)
            izbrani = urejene_povezave[:st]
            nakljucni = random.choice(izbrani)
            (prvi,drugi) = nakljucni
            vi = drugi
            priblizek[i] = vi
            mesta.remove(vi)
        dolzina = 0
        for i in range(1,n):
            dolzina += slovar[(priblizek[i],priblizek[i+1])]
        priblizek[0] = dolzina
        zacetni_priblizki[j] = priblizek
    return zacetni_priblizki
    
    #vsak začetni približek t = (l,1,v2,...,vn) iz RCL konstruiramo tako, da
    #določimo v1 := 1 nato iterativno za i = 2,...,n za vi izberemo naključno
    #med n/5 (celi del) najbližjih vozlišč do vi-1, ki še niso v t
    #take cikle t konstruiramo toliko časa, da RCL napolnimo
def local_search(g,k, iter):
    RCL = grasp(g,k)
    RCL.sort(key=lambda x: x[0])
    stevec = 0
    while stevec < iter:
        utezi = [... for i in range(0,k)]
        t = random.choice(RCL, 1, utezi)
        

    #elementi v RCL so urejeni po dolžini, primerjamo jih po l
    #naključno izberemo t v RCL, toda z linearno padajočo verjetnostjo
    #najverjetneje izbereme cikel na vrhu RCL - najkrajši
    #okolico cikla t definiramo kot monožico vseh ciklov t' iz CL, ki jih dobimo
    #iz t tako, da mu zamenjamo dve vozišči
    #torej naključno zamenjamo dve vozlišči t
    #preverimo če smo s tem dobili krajši cikel
    #če ja, t odstranimo iz RCL in dodamo t'
    #ponavaljamo tolikokrat kot je predpisano



