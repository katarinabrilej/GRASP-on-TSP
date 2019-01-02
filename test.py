import random
import numpy as np

# izboljšaj funkcijo

# N je število mest (torej dimenzija incidenčne matrike)
# max_pot je največja razdalja / cena poti
def TSP(N, max_pot, min_pot = 1):
    " funkcija vrne naključno matriko cen povezav, ki predstavlja problem potujočega trgovca"
    a = np.random.randint(min_pot, max_pot, size= (N,N))
    m = np.tril(a) + np.tril(a, -1).T
    for i in range(N):
        m[i][i] = 0
    return m


#import ilp as ILP
import GRASP as GRASP
import uvoz as uv

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

M = [[ 0,  9,  8, 2,  2,  9, 8, 9, 7, 8],
    [ 9,  0,  7,  9, 8,  4,  7, 9,  8,  2],
    [8, 7, 0, 9, 8, 9, 3, 2, 7, 9],
     [2,9,9,0,9,8,7,9,8,1],
     [2,8,8,9,0,9,3,8,7,9],
     [9,4,9,8,9,0,9,8,1,7],
     [8,7,3,7,3,9,0,9,8,9],
     [9,9,2,9,8,8,9,0,3,8],
     [7,8,7,8,7,1,8,3,0,9],
     [8,2,9,1,9,7,9,8,9,0]]


#GRASP.local_search(M, 5, 100, "dva_opt")
#GRASP.local_search(l, 10, 100, "dva_opt")
#GRASP.local_search(l, 10, 100, "tri_opt")  
