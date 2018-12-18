from pulp import *
import numpy as np
import random #mogoče ne rabim

#Izmišljena mesta
sites = ['org','A','B','C']
#non symetric distances
distances = dict( ((a,b),np.random.randint(10,50)) for a in sites for b in sites if a!=b )

#Definiramo problem
prob=LpProblem("salesman",LpMinimize)

# Dummy, 1 = če je mesto i točno pred mestom j na poti (mesti i in j sta povezani)
x = LpVariable.dicts('x',distances, 0,1,LpBinary)

# kar minimiziramo:
cost = lpSum([x[(i,j)]*distances[(i,j)] for (i,j) in distances])
prob+=cost

#pri pogojih:
for k in sites:
    #Vsako mesto ima točno eno vhodno povezavo:
    prob+= lpSum([ x[(i,k)] for i in sites if (i,k) in x]) ==1
    #Vsako mesto ima točno eni izhodno povezavo:
    prob+=lpSum([ x[(k,i)] for i in sites if (k,i) in x]) ==1

#we need to keep track of the order in the tour to eliminate the possibility of subtours
#Da bi preprečili več ciklov kot enega, moramo beležiti še zaporedje potovanja
u = LpVariable.dicts('u', sites, 0, len(sites)-1, LpInteger)

#Želimo le en cikel:
N=len(sites)
for i in sites:
    for j in sites:
        if i != j and (i != 'org' and j!= 'org') and (i,j) in x:
            prob += u[i] - u[j] <= (N)*(1-x[(i,j)]) - 1
            
sites_left = sites.copy()
org = 'org'
tour=[]
tour.append(sites_left.pop( sites_left.index(org)))

while len(sites_left) > 0:
    
    for k in sites_left:
        if x[(org,k)].varValue ==1:
            tour.append( sites_left.pop( sites_left.index(k)))
            org=k
            break
            
tour.append('org')

tour_legs = [distances[(tour[i-1], tour[i])] for i in range(1,len(tour))]

print('Našel sem optimalno pot!')
print(' -> '.join(tour))
sum(tour_legs)
