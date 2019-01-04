import random
import numpy as np

def slovar_razdalj(g):
    "funkcija sprejme incidenčno matriko razdalj/cen povezav in vrne slovar katerega elementi imajo "
    " za ključ povezavo oblike (v_i,v_j), za vrednost pa razdaljo med v_i in v_j"
    r = range(len(g))
    razdalja = {(i+1, j+1): g[i][j] for i in r for j in r}
    return razdalja
    
def dolzina_poti(slovar,n,pot):
    " funkcija sprejme slovar razdalj in pot v grafu ter vne dolžino poti"
    dolzina = 0
    for i in range(1,n):
            dolzina += slovar[(pot[i],pot[i+1])]
    dolzina += slovar[(pot[n],pot[1])]
    return dolzina


# greedy randomized construction

# slovar je slovar_razdalj incidenćne matrike g, ki predstavlja graf
# parameter alpha, določa moč množice RCL (restricted client list) ali v tem primeru dolžino seznama RCL
# z drugimi besedami: alpha določa število začetnih približkov, ki jih konstruira greedy construction
# množica vseh rešitev CL (client list) je množica vseh Hamiltonovih ciklov v g
# predstavimo jih kot zaporedja števil (l,1,v2,...,vn)

def greedy_construction(slovar,n, alpha):
    " funkcija sprejme matriko g, parameter in alpha "
    RCL = [0] * alpha
    if n > 5: # p mora biti vsaj 1
        p = n // 5 
    else:
        p = 1
    # začetnih približkov konstruiramo toliko kot je vrednost alpha
    for j in range(0, alpha):
        # vsak začetni približek t = (l,1,v2,...,vn) iz RCL konstruiramo tako, da
        # določimo v1 := 1 
        t = [0] * (n+1)
        t[1] = 1
        mesta = [h for h in range(2,n+1)] #vsa možna mesta v grafu
        for i in range(2,n+1):
            # iterativno za i = 2,...,n za vi izberemo naključno
            # med p % najbližjih vozlišč do vi-1, ki še niso v t
            povezave = [(t[i-1],m) for m in mesta] # vse možne povezave v grafu
            slovar_povezav = { key:value for key, value in slovar.items() if key in povezave }
            # slovar_povezav v katerem so zabeležene povezave z mesti, ki jih še nismo obiskali
            urejene_povezave = sorted(slovar_povezav, key=slovar_povezav.__getitem__)
            (_,vi) = random.choice(urejene_povezave[:p]) # naključno izberemo naslednje vozlišče v t
            t[i] = vi
            mesta.remove(vi) # mesto odstranimo iz seznama mest
        t[0] = dolzina_poti(slovar,n,t) # l oz. t[0] je dolžina cikla (1,v2,...,vn) v grafu g
        RCL[j] = t # cikel t dodamo v seznam RCL
    return RCL # vrnemo množico začetnih približkov RCL 
    
# local search lahko izvajamo na dva načina, z metodo 2-opt ali pa 3-opt

# 2-opt
# Metoda poizkuša izboljšati izbrani cikel iz RCL tako, da naključno zamenjamo dve vozlišči t.
# Namesto da shranjujemo vse možne cikle in njihove dolžine ter na koncu pogledamo, če je najkrajši boljši kot t,
# raje sproti računamo kakšno razliko v dolžini bi prinesla določena menjava mest. 

def dva_opt(n, t, slovar):
    " funkcija sprejme slovar razdalj grafa g, velikost grafa ter naključno izbrani cikel t iz RCL."
    " Če uspe rešitev izboljšati, vrne krajši cikel novi_t." 
    razlika = 0
    for i in range(2,n):
        for j in range(i+1,n+1):
            if j != n: # poveza s + dodamo, povezave z - pa odstranimo/prekinemo
                change = slovar[(t[i-1],t[j])] + slovar[(t[i],t[j+1])] - slovar[(t[i-1],t[i])] - slovar[(t[j],t[j+1])]
            else: # v primeru, da je j = n, prekinemo razdaljo od vozlišča j do vozlišča 1 
                change = slovar[(t[i-1],t[j])] + slovar[(t[i],t[1])] - slovar[(t[i-1],t[i])] - slovar[(t[j],t[1])]
            # če smo uspeli z menjavo izboljšati dolžino poti    
            if change < razlika:
                razlika = change # posodobimo razliko
                opt_i =  i # zabeležimo optimalni i 
                opt_j = j # in optimalni j 
    if razlika < 0: # če nam v celotnem postopku uspelo izboljšati cikel
        novi_t = [t[m] for m in range(0,n+1)] # novi_t je enak t z izjemo menjave v naslednjem koraku
        novi_t[opt_i:opt_j+1] = novi_t[opt_i:opt_j+1][::-1] # izvedemo menjavo od i-tega do j-tega mesta
        novi_t[0] = t[0] + razlika  # dolžini t zdaj prištejemo razliko (ki je negativna), da dobimo dolžino novi_t     
        return novi_t
    else:
        return None # če nam ni uspelo izboljšati cikla, vrnemo None

# 3-opt
# Z metodo 3-opt cikel prekinemo na treh mestih. Tako nastale dele lahko nazaj povežemo na 7 načinov (+1, ki je identiteta)
# 3 od teh so oblike 2-opt, saj eno izmed prekinjenih povezav sestavimo nazaj, pri preostalih štirih pa dejansko prekinemo vse 3 povezave
# Metoda je podobna kot 2-opt, ker pa pregleda večjo okolico, doda več fleksibilnosti v spreminjanju trenutnega cikla.
# Boljšo rešitev lahko tako vrne v primeru, ko se je 2-opt algoritem znašel v lokalnem minimumu iz katerega ne more ven,v tem primeru pa lahko
# in morda vrne boljšo rešitev

# menjava je odvisna in indeksa, ki določa katera menjava se bo izvedla, trenutnega cikla in njegove velikosti ter optimalnih i,j,k
# pri katerih je bila dosežena minimalna razlika (torej največja po abs vrednosti) 
def menjava(indeks,n,t,opt_i,opt_j,opt_k):
    " funkcija na danem ciklu izvrši ustrezno menjavo v odvisnosti od indeksa in optimalnih i,j in k)"
    novi_t = [t[m] for m in range(0,n+1)] # novi_t spet izhaja iz t
    # odvisno od indeksa naredimo ustrezno menjavo
    # menjave od 1 do 3 so 2-opt, od 4 naprej so 3-opt
    if indeks == 1:
        novi_t[opt_i:opt_k] = novi_t[opt_i:opt_k][::-1] # povezana ostaneta Y1 in Y2, prekinemo pa povezavi (X1, X2) in (Z1, Z2)
                                                        # tako da dobimo povezavi (X1, Z1) in (X2, Z2)        
    if indeks == 2:
        novi_t[opt_j:opt_k] = novi_t[opt_j:opt_k][::-1] # povezana ostaneta X1 in X2, prekinemo pa povezavi (Y1 Y2) in (Z1, Z2)
                                                        # tako da dobimo povezavi (Y1 ,Z1) in (Y2 Z2) 
    if indeks == 3:
        novi_t[opt_i:opt_j] = novi_t[opt_i:opt_j][::-1] # povezana ostaneta Z1 in Z2, prekinemo pa povezavi (X1 X2) in (Y1, Y2)
                                                        # tako da dobimo povezavi (X1, Z1) in (X2, Z2)       
    # v vse naslednjih primerih prekinemo  povezave (X1, X2), (Y1, Y2) in (Z1, Z2)
    if indeks == 4:
        novi_t[opt_i:opt_j] = novi_t[opt_i:opt_j][::-1] # nove povezave (X1, Z1),(Y2, X2) in (Y1, Z1) dobimo tako da obrnemo del cikla
        novi_t[opt_j:opt_k] = novi_t[opt_j:opt_k][::-1] # med Y1 in X2 ter Z1 in Y2      
    if indeks == 5:
        tmp = novi_t[opt_j:opt_k][::-1] + novi_t[opt_i:opt_j] # nove povezave (X1, Y1),(X2, Z1) in (Y2, Z2) dobimo tako da obrnemo del cikla
        novi_t[opt_i:opt_k] = tmp                             # med Y2 in Z1, ga združimo z delom med X2 in Y1 (damo pred)                           
    if indeks == 6:
        tmp = novi_t[opt_j:opt_k] + novi_t[opt_i:opt_j][::-1] # nove povezave (X1, Y2), (Z1, Y1) in (X2, Z2) dobimo tako da obrnemo del cikla
        novi_t[opt_i:opt_k] = tmp                             # med X2 in Y1, ga združimo z delom med Y2 in Z1 (damo za)   
    if indeks == 7:
        tmp = novi_t[opt_j:opt_k] + novi_t[opt_i:opt_j] # nove povezave (X1, Y2), (Z1, X2) in (Y1, Z2) dobimo tako, da skupaj združimo del cikla
        novi_t[opt_i:opt_k] = tmp                       # med Y2 in Z1 ter med X2 in Y1 
    return novi_t # vrnemo izboljšan cikel
        
# Pri računanju razlik postopamo podobno kot pri 2-opt. Zopet sproti računamo razliko, ki jo z določeno menjavo dosežemo,
# ker pa je menjav več, moramo izračunati več razlik. 

def tri_opt(n, t, slovar):
    " funkcija sprejme slovar razdalj grafa g, velikost grafa ter naključno izbrani cikel t iz RCL."
    " Če uspe rešitev izboljšati, vrne krajši cikel novi_t." 
    razlika = 0    
    for i in range(2,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                # zaradi preglednosti definiramo nove spremenljivke
                X1, X2, Y1, Y2, Z1, Z2 = t[i-1], t[i], t[j-1], t[j], t[k-1], t[k]
                # 2 opt moves
                change1 = slovar[(X1,Z1)] + slovar[(X2,Z2)] -  slovar[(X1,X2)] - slovar[(Z1,Z2)]
                change2 = slovar[(Y1, Z1)] + slovar[(Y2, Z2)] -  slovar[(Y1, Y2)] - slovar[(Z1, Z2)] 
                change3 = slovar[(X1, Y1)] + slovar[(X2, Y2)] -  slovar[(X1, X2)] - slovar[(Y1, Y2)]
                # 3 opt moves
                odstej = slovar[(X1, X2)] + slovar[(Y1, Y2)] + slovar[(Z1, Z2)]
                # v vseh treh primerih odstranimo enake povezave
                change4 = slovar[(X1, Y1)] + slovar[(X2, Z1)] + slovar[(Y2, Z2)] -  odstej
                change5 = slovar[(X1, Z1)] + slovar[(Y2, X2)] + slovar[(Y1, Z2)] -  odstej
                change6 = slovar[(X1, Y2)] + slovar[(Z1, Y1)] + slovar[(X2, Z2)] -  odstej
                change7 = slovar[(X1, Y2)] + slovar[(Z1, X2)] + slovar[(Y1, Z2)] -  odstej
                # izberemo najmanjšo spremembo 
                spremembe = [change1,change2,change3, change4, change5,change6,change7]
                change = min(spremembe)
                ind = np.argmin(spremembe) + 1 # zabeležimo indeks optimalne spremembe, saj nam bo ta povedal katero menjavo moramo narediti
                if change < razlika:
                    razlika = change
                    indeks = ind
                    opt_i =  i # zabeležimo optimalne i,j in k 
                    opt_j = j
                    opt_k = k
    if razlika < 0: # če smo uspeli izboljšati cikel
        novi_t = menjava(indeks,n,t,opt_i,opt_j,opt_k) # izvedemo ustrezno menjavo
        novi_t[0] = t[0] + razlika # posodobimo dolžino cikla
        return novi_t
    else:
        return None

# vhodni podatki za algoritem so graf g z vozlišči od 1 do n, ki je podan v obliki incidenčne matrike
# (g_ij torej predstavlja razdaljo med mestoma i in j)
# ter parameter alpha, iter kot število dovoljenih iteracij algoritma, metoda je lahko dva_opt ali tri_opt

def local_search(g,alpha,iter, metoda):
    " fukcija vrne najkrajši cikel v grafu g po iter ponovitvah. uporabimo dano metodo in konstruira alpha začetnih približkov " 
    n = len(g)
    slovar = slovar_razdalj(g) # matriko g pretvorimo v slovar razdalj
    RCL = greedy_construction(slovar,n,alpha) # ustvarimo seznam začetnih približkov dolžine alpha
    RCL.sort(key=lambda x: x[0]) # seznam začetnih približkov uredimo glede na dolžino poti, od najkrajšega do najdaljšega
    stevec = 0
    while stevec < iter: # začetne približke izbljšujemo dokler ne dosežemo predpisanega števila iteracij
        utezi = [i * 2/((alpha+1)*alpha) for i in range(alpha,0,-1)]
        indeks = np.random.choice(len(RCL), size = 1, p = utezi) # naključno izberemo t v RCL, toda z linearno padajočo verjetnostjo
        # najverjetneje izbereme cikel na vrhu RCL (najkrajši)
        t = RCL[indeks[0]]
        # različno iskanje približka glede na metodo
        if metoda == "dva_opt":
            novi_t = dva_opt(n,t,slovar)
        elif metoda == "tri_opt":
            novi_t = tri_opt(n,t,slovar)
        # če smo uspeli izboljšati rešitev, torej dobiti krajši cikel
        if novi_t:
            RCL.append(novi_t) # dodamo nov cikel
            RCL.remove(t) # in odstranimo starega
        stevec += 1
        RCL.sort(key=lambda x: x[0]) # zopet uredimo RCL
    return RCL[0] # vrnemo najkrajši cikel
