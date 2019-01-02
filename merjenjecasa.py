import time

def cas_ilp(matrika):
    start = time.time()
    tsp_as_ilp(matrika)
    end = time.time()
    return end - start

def cas_grasp(matrika,k,iter):
    start = time.time()
    local_search(matrika,k,iter, "tri_opt")
    end = time.time()
    return end - start
