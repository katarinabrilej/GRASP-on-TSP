#import ilp as ILP
import GRASP as GRASP

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


matrika = [[0, 3, 9, 2, 11],
           [3, 0, 10, 9, 2],
           [9, 10, 0, 3, 4],
           [2, 9, 3, 0, 11],
           [11, 2, 4, 11, 0]]

zgled = GRASP.TSP(10,50)
