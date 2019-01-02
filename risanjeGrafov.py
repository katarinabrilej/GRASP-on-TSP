import networkx as nx # in cmd write: pip install networkx
import math
import matplotlib.pyplot as plt
import numpy as np
import os

## Risanje omrežja kot v "teoriji grafov" (Z utežmi na povezavah):

def ustvarigraf(matrika):
    G = nx.Graph()
    for i in range(len(matrika)):
        for j in range(len(matrika))[i:] :
            if matrika[i][j] > 0:
                G.add_edge(i+1, j+1, length = matrika[i][j])
    return G

def narisigraf(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True, edge_color = 'black')  #with_labels=true is to show the node number in the output graph
	edge_labels = nx.get_edge_attributes(G,'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels,  font_size = 11) #napiše uteži na povezave
	return pos, plt.show()
    
def resitev_v_matriko(m, resitev):
    "resitev metode GRASP (local search) pretvori v matriko"
    prazna = np.zeros((len(m), len(m)))
    for k in resitev[1:-1]:
        prazna[k-1][resitev[resitev.index(k)+1]-1] = m[k-1][resitev[resitev.index(k)+1]-1]
        prazna[resitev[resitev.index(k)+1]-1][k-1] = m[resitev[resitev.index(k)+1]-1][k-1]
    prazna[resitev[-1]-1][0] = m[resitev[-1]-1][0]
    prazna[0][resitev[-1]-1]= m[0][resitev[-1]-1]
    return prazna

def narisi_graf(matrika):
    G = ustvarigraf(matrika)
    return narisigraf(G)

## Risanje omrežja z upoštevanjem koordinat (v 2D):

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
    
# koord = preberi_koordinate("berlin52.tsp",52,6)

def uredi_mesta(koord, resitev):
    "uredi seznam s koordinatami mest v vrstni red optimalne poti"
    resitev = resitev[1:]
    nove =[]
    for i in resitev:
        nove.append(koord[i-1])
    nove.append(nove[0])
    return nove

def narisi(positions, resitev):
    "positions = seznam, ki ga vrne funkcija preberi_koordinate,"
    "resitev = seznam, ki ga vrne algoritem GRASP"
    positions = uredi_mesta(positions, resitev)
    positions = np.array(positions)
    fig, ax = plt.subplots(2, sharex=True, sharey=True)  # Prepare 2 plots
    ax[0].set_title('Mesta')
    ax[1].set_title('Optimalna pot')
    ax[0].scatter(positions[:, 1], positions[:, 2])             # plot A
    ax[1].scatter(positions[:, 1], positions[:, 2])             # plot B
    ax[1].plot(positions[:, 1], positions[:, 2])                # plot B
    plt.tight_layout()
    plt.show()


