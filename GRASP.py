import random
import numpy as np

# g je matrika cen povezav 
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
    dolzina += slovar[(pot[n],pot[1])]
    return dolzina

# greedy randomized construction

# vsak začetni približek t = (l,1,v2,...,vn) iz RCL konstruiramo tako, da
# določimo v1 := 1 nato iterativno za i = 2,...,n za vi izberemo naključno
# med p % najbližjih vozlišč do vi-1, ki še niso v t
# take cikle t konstruiramo toliko časa, da RCL napolnimo
    
def greedy_construction(g, alpha):
    RCL = [0] * alpha
    slovar = slovar_cen(g)
    n = len(g)
    p = n // 2  # n//nekaj mora biti vec kot 1 
    for j in range(0, alpha):
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

def dva_opt(n, t,g):
    slovar = slovar_cen(g)
    razlika = 0
    for i in range(2,n):
        for j in range(i+1,n+1):
            if j != n:
                change = slovar[(t[i-1],t[j])] + slovar[(t[i],t[j+1])] - slovar[(t[i-1],t[i])] - slovar[(t[j],t[j+1])]
            else:
                change = slovar[(t[i-1],t[j])] + slovar[(t[i],t[1])] - slovar[(t[i-1],t[i])] - slovar[(t[j],t[1])]
                
            if change < razlika:
                razlika = change
                opt_i =  i
                opt_j = j

    if razlika < 0:
        novi_t = [t[m] for m in range(0,n+1)]
        novi_t[opt_i:opt_j+1] = novi_t[opt_i:opt_j+1][::-1]

        novi_t[0] = t[0] + razlika        
        return novi_t
    else:
        return None


def menjava(indeks,n,t,opt_i,opt_j,opt_k):
    
    novi_t = [t[m] for m in range(0,n+1)]
    
    if indeks == 1:
        novi_t[opt_i:opt_k] = novi_t[opt_i:opt_k][::-1]
    if indeks == 2:
        novi_t[opt_j:opt_k] = novi_t[opt_j:opt_k][::-1]
    if indeks == 3:
        novi_t[opt_i:opt_j] = novi_t[opt_i:opt_j][::-1]
        
    if indeks == 4:
        novi_t[opt_i:opt_j] = novi_t[opt_i:opt_j][::-1]
        novi_t[opt_j:opt_k] = novi_t[opt_j:opt_k][::-1]
        
    if indeks == 5:
        tmp = novi_t[opt_j:opt_k][::-1] + novi_t[opt_i:opt_j]
        novi_t[opt_i:opt_k] = tmp
        
    if indeks == 6:
        tmp = novi_t[opt_j:opt_k] + novi_t[opt_i:opt_j][::-1]
        novi_t[opt_i:opt_k] = tmp
        
    if indeks == 7:
        tmp = novi_t[opt_j:opt_k] + novi_t[opt_i:opt_j]
        novi_t[opt_i:opt_k] = tmp
    return novi_t
        

def tri_opt(n, t, g):
    #print("nova iteracija")
    slovar = slovar_cen(g)
    razlika = 0
    
    for i in range(2,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                X1, X2, Y1, Y2, Z1, Z2 = t[i-1], t[i], t[j-1], t[j], t[k-1], t[k]


# 2 opt moves
                change1 = slovar[(X1,Z1)] + slovar[(X2,Z2)] -  slovar[(X1,X2)] - slovar[(Z1,Z2)]
                change2 = slovar[(Y1, Z1)] + slovar[(Y2, Z2)] -  slovar[(Y1, Y2)] - slovar[(Z1, Z2)] 
                change3 = slovar[(X1, Y1)] + slovar[(X2, Y2)] -  slovar[(X1, X2)] - slovar[(Y1, Y2)]
# 3 opt moves
                odstej = slovar[(X1, X2)] + slovar[(Y1, Y2)] + slovar[(Z1, Z2)]

                change4 = slovar[(X1, Y1)] + slovar[(X2, Z1)] + slovar[(Y2, Z2)] -  odstej
                change5 = slovar[(X1, Z1)] + slovar[(Y2, X2)] + slovar[(Y1, Z2)] -  odstej
                change6 = slovar[(X1, Y2)] + slovar[(Z1, Y1)] + slovar[(X2, Z2)] -  odstej
                change7 = slovar[(X1, Y2)] + slovar[(Z1, X2)] + slovar[(Y1, Z2)] -  odstej

                spremembe = [change1,change2, change3, change4, change5,change6,change7]
                change = min(spremembe)
                ind = np.argmin(spremembe) + 1

                if change < razlika:
##                    print("negativnoooo")
##                    print(t)
##                    print(i)
##                    print(j)
##                    print(k)
##                    print(change)
##                    print("indeks")
##                    print(ind)
                    razlika = change
                    indeks = ind
                    opt_i =  i
                    opt_j = j
                    opt_k = k

    if razlika < 0:
        novi_t = menjava(indeks,n,t,opt_i,opt_j,opt_k)
        novi_t[0] = t[0] + razlika
##        print("novi_T")
##        print(novi_t)
        return novi_t
    else:
        return None
            

def local_search(g,k,iter, metoda):
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

        if metoda == "dva_opt":
            novi_t = dva_opt(n,t,g)
        elif metoda == "tri_opt":
            novi_t = tri_opt(n,t,g)
        
        if novi_t:
            RCL.append(novi_t)
            RCL.remove(t)   
        stevec += 1
        RCL.sort(key=lambda x: x[0])
    RCL.sort(key=lambda x: x[0])
    return RCL[0]

