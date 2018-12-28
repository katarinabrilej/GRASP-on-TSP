
from pulp import *
import numpy as np

# g je matrika cen povezav
def slovar_cen(g):
    r = range(len(g))
    cena = {(i+1, j+1): g[i][j] for i in r for j in r}
    #izbrišemo cene diagonalnih elementov:
    for k in range(len(g)+1):
        for key in [key for key in cena if key == (k,k)]: del cena[key]
    return cena

def tsp_as_ilp(g):
    " Funkcija reši problem trgovskega potnika s celoštevilskim linearnim programiranjem."
    " Sprejme matriko cen povezav, izpiše pa minimalno razdaljo/ceno potovanja "
    " in vrne urejen seznam obiskanih mest. "
    razdalje = slovar_cen(g) # slovar razdalj
    mesta = [x+1 for x in range(len(g))]  # seznam mest (od 1 do n)
    prob=LpProblem("salesman", LpMinimize) # definiramo problem

    #  Dummy, 1 = če je mesto i točno pred mestom j na poti (mesti i in j sta povezani):
    x = LpVariable.dicts('x', razdalje, 0,1, LpBinary)
    
    cena = lpSum([x[(i,j)]*razdalje[(i,j)] for (i,j) in razdalje]) # to minimizramo
    prob+=cena

    # pri pogojih:
    for k in mesta:
        #Vsako mesto ima točno eno vhodno povezavo:
        prob+= lpSum([ x[(i,k)] for i in mesta if (i,k) in x]) == 1
        #Vsako mesto ima točno eno izhodno povezavo:
        prob+= lpSum([ x[(k,i)] for i in mesta if (k,i) in x]) == 1
    #pri zgornjih pogojih velja: i=/=j, vendar smo te povezave že izbrisali v slovarju cen    

    #Da bi preprečili več ciklov kot enega, moramo beležiti še zaporedje potovanja:
    u = LpVariable.dicts('u', mesta, 0, len(mesta)-1, LpInteger)

    #Želimo le en cikel:
    N=len(mesta)
    for i in mesta:
        for j in mesta:
            if i != j and (i != 1 and j!= 1) and (i,j) in x:
                prob += u[i] - u[j] <= (N)*(1-x[(i,j)]) - 1

    prob.solve()
   # print(LpStatus[prob.status]) #želimo "optimal"
    
    sites_left = mesta.copy()
    org = 1 #(začnemo v mestu 1)
    potovanje=[]
    potovanje.append(sites_left.pop(sites_left.index(org)))
    
    while len(sites_left) > 0:
    
        for k in sites_left:
            if x[(org,k)].varValue == 1:
                potovanje.append(sites_left.pop(sites_left.index(k)))
                org=k
                #break
            
    potovanje.append(1)
    
    #Vrednost spremenljivk:
    #for v in prob.variables():
    #    print(v.name, "=", v.varValue)
    
    print("Optimalna cena potovanja = ", value(prob.objective))
    
    return potovanje
    
