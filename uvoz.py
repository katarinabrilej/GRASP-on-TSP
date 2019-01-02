import random
import numpy as np

# funkcija trenutno razdalje računa, kot da bi bile v koordinatnem sistemu in ne na krogli
# popravi !!!

# v datoteki so v posamezni vrstici napisani zaporedna številka mesta ter koordinate
def matrika_razdalj(datoteka):
    " funkcija sprejme množico mest in njihove koordinate ter izračuna razdalje med mesti, ki jih "
    " zabeleži v matriko "
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



with open("swiss42.tsp", 'r') as f:
    vsebina = f.readlines()
    st_mest = 42
    matrika = np.zeros(shape=(st_mest, st_mest))
    vsebina = vsebina[7:49]


    l = [[int(num) for num in line.strip().split()] for line in vsebina ]

