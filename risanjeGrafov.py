import networkx as nx # in cmd write: pip install networkx
import matplotlib.pyplot as plt

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


def narisi_graf(matrika):
    G = ustvarigraf(matrika)
    return narisigraf(G)


# def resitev_v_matriko(m, resitev):
# v bodoce: napisi se funkcijo, ki resitev iz ilp in grasp spremeni v matriko
# tako, da bomo lahko narisali se resitev

    
def resitev_v_matriko(m, resitev):
    "resitev metode GRASP (local search) pretvori v matriko"
    prazna = np.zeros((len(m), len(m)))
    for k in resitev[1:-1]:
        prazna[k-1][resitev[resitev.index(k)+1]-1] = m[k-1][resitev[resitev.index(k)+1]-1]
        prazna[resitev[resitev.index(k)+1]-1][k-1] = m[resitev[resitev.index(k)+1]-1][k-1]
    prazna[resitev[-1]-1][0] = m[resitev[-1]-1][0]
    prazna[0][resitev[-1]-1]= m[0][resitev[-1]-1]
    return prazna
        
#dodaj se risanje koordinat  
    
