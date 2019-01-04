import GRASP as GRASP
import ilp as ILP
import uvoz as uv
import risanjeGrafov as rg
import merjenjecasa as mc
import primerjava as pr

# 1. UVOZ

## uv.preberi_matriko(datoteka,velikost,k=7) #primer swiss42
# swiss42 = uv.preberi_matriko("swiss42.tsp",42)

## uv.preberi_koordinate(datoteka, velikost, k)

## uv.geo_razdalje(datoteka, velikost, k=7) #primer ulysses22
# ulysses22 = uv.geo_razdalje("ulysses22.tsp",22)

## uv.razdalje(datoteka, velikost,k=6) #primeri berlin52, kroA100, st70
# berlin52 = uv.razdalje("berlin52.tsp",52)

#funkciji razdalje in geo_razdalje vrneta matriko, ki jo potrebujemo pri reševanju (točka 2)
#funkcija preberi_koordinate vrne seznam, ki ga potrebujemo pri risanju (točka 3)

# 2. REŠEVANJE

# a) Grasp

##GRASP.slovar_razdalj(g)
##GRASP.dolzina_poti(slovar,n,pot)
##GRASP.local_search(g,alpha,iter, metoda)

# local_search je funkcija, ki zažene algoritem in vrne najkrajšo pot

# metoda je lahko dva_opt ali tri_opt
# g je incidenčna matrika
# iter je število iteracij
# alpha je število začetni približkov (moč RCL)
# slovar je slovar razdalj
# n je velikost matrike/grafa/cikla

## pr.povprecje(ponovitve,g,k,iter,metoda)
# funkcija vrne povprečje cen pri določenemu številu ponovitev in najboljšo pot
# pr.povprecje(10,berlin52,3,100,"dva_opt")


# b) Ilp

##ILP.slovar_cen_ilp(g)
##ILP.tsp_as_ilp(g)

# tsp_as_ilp(g): Sprejme matriko cen povezav (g), izpiše minimalno
#      razdaljo/ceno potovanja in vrne urejen seznam obiskanih mest.

# 3. RISANJE:

# koord = uv.preberi_koordinate("berlin52.tsp",52,6)
# resitev = GRASP.local_search(g,alpha,iter,metoda)

## rg.uredi_mesta(koord, resitev)
## rg.narisi(koord, resitev)

# 4. MERJENJE ČASA IZVAJANJA:

## mc.cas_ilp(matrika)

## mc.cas_grasp(matrika,k,iter,metoda)

