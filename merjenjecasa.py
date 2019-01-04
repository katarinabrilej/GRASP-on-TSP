import time
import ilp as ILP
import GRASP as GRASP

def cas_ilp(matrika):
    start = time.time()
    ILP.tsp_as_ilp(matrika)
    end = time.time()
    return end - start

def cas_grasp(matrika,k,iter,metoda):
    start = time.time()
    GRASP.local_search(matrika,k,iter,metoda)
    end = time.time()
    return end - start

#Če želimo, da cas_grasp() vrne še dobljeno rešitev:

#def cas_grasp(matrika,k,iter,metoda):
#    start = time.time()
#    resitev = GRASP.local_search(matrika,k,iter,metoda)
#    end = time.time()
#    return end - start, resitev
