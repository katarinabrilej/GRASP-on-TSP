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

def narisigraf(matrika):
    G = ustvarigraf(matrika)
    pos = nx.circular_layout(G) # izberi med kamada_kawai_layout, spring_layout, circular_layout itd..
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


## Risanje omrežja z upoštevanjem koordinat (v 2D):

import uvoz as uv

# koord = uv.preberi_koordinate("berlin52.tsp",52,6)
# koord = uv.preberi_koordinate("ulysses22.tsp",22,6)

def uredi_mesta(koord, resitev):
    "uredi seznam s koordinatami mest v vrstni red optimalne poti"
    resitev = resitev[1:]
    nove =[]
    for i in resitev:
        nove.append(koord[i-1])
    nove.append(nove[0])
    return nove

def narisi(koord, resitev):
    "positions = seznam, ki ga vrne funkcija preberi_koordinate,"
    "resitev = seznam, ki ga vrne algoritem GRASP"
    koord = uredi_mesta(koord, resitev)
    koord = np.array(koord)
    fig, ax = plt.subplots(2, sharex=True, sharey=True)  # Prepare 2 plots
    ax[0].set_title('Mesta')
    ax[1].set_title('Optimalna pot')
    ax[0].scatter(koord[:, 1], koord[:, 2])             # plot A
    ax[1].scatter(koord[:, 1], koord[:, 2])             # plot B
    ax[1].plot(koord[:, 1], koord[:, 2])                # plot B
    plt.tight_layout()
    plt.show()


