import GRASP as GRASP
import uvoz as uv

# funkcije

# GRASP.dolzina_poti(slovar,pot)
# GRASP.local_search(g,k,iter, metoda)



# primeri od skupine 7 
ulysses22 = uv.ulysses22
berlin52 = uv.berlin52
kroA100 = uv.kroA100

# primeri
swiss42 = uv.swiss42
st70 = uv.st70 

# tako kot v algoritmu g predstavlja matriko za TSP, iter število dovoljeni iteracij algoritma
# alpha število začetnih približkov, metoda je lahko 2-opt ali pa 3-opt. 
def povprecje(ponovitve,g,alpha,iter, metoda):
    " funkcija vrne povprečje dolžin poti/cikla pri danem številu ponovitev algortima GRASP "
    " vrne tudi minimalno dolžino in najboljšo pot "
    min_pot = GRASP.local_search(g,alpha,iter, metoda)
    min_resitev = min_pot[0]
    vsota = min_resitev
    for i in range (ponovitve-1):
        resitev = GRASP.local_search(g,alpha,iter, metoda)
        l = resitev[0]
        vsota += l
        if l < min_resitev:
            min_resitev = l
            min_pot = resitev       
    povprecje = vsota / ponovitve
    return (povprecje, min_resitev, min_pot)

# primerjava rezultatov za različne vrednosti parametra alpha

# ulysses22 velikosti 22x22
# ponovitve = 10, iter = 100
# 7013 je znana optimalna rešitev

# dva_opt

##povprecje(10,ulysses22,3,100,"dva_opt") # best = 7013
##povprecje(10,ulysses22,5,100,"dva_opt") # best = 7013
##povprecje(10,ulysses22,10,100,"dva_opt") # best = 7013
##povprecje(10,ulysses22,15,100,"dva_opt") # best = 7013

# vedno vrne optimalno vrednost 7013, neodvisno od parametra alfa

# tri_opt

##povprecje(10,ulysses22,3,100,"tri_opt") # best = 7013
##povprecje(10,ulysses22,5,100,"tri_opt") # best = 7013
##povprecje(10,ulysses22,10,100,"tri_opt") # best = 7013
##povprecje(10,ulysses22,15,100,"tri_opt") # best = 7013

# swiss42 velikosti 42x42
# ponovitve = 10, iter = 100
# 1273 je znana optimalna rešitev 

# dva_opt

##povprecje(10,swiss42,3,100,"dva_opt") # best = 1273
##povprecje(10,swiss42,5,100,"dva_opt") # best = 1273
##povprecje(10,swiss42,10,100,"dva_opt") # best = 1420
##povprecje(10,swiss42,15,100,"dva_opt") # best = 1592

# tri_opt

##povprecje(10,swiss42,3,100,"tri_opt") # best = 1273
##povprecje(10,swiss42,5,100,"tri_opt") # best = 1273
##povprecje(10,swiss42,10,100,"tri_opt") # best = 1316
##povprecje(10,swiss42,15,100,"tri_opt") # best = 1273

#opt pot: [1273, 1, 33, 35, 34, 21, 36, 37, 32, 18, 8, 38,
#16, 17, 15, 20, 14, 6, 27, 19, 13, 12, 26,
#11, 9, 42, 24, 10, 22, 41, 25, 40, 23, 39, 31, 30, 29, 3, 28, 4, 5, 7, 2]


# berlin52 velikosti 52x52
# ponovitve = 10, iter = 100
# 7542 je znana optimalna rešitev

# dva_opt

##povprecje(10,berlin52,3,100,"dva_opt") # best = 7716
##povprecje(10,berlin52,5,100,"dva_opt") # best = 8130
##povprecje(10,berlin52,10,100,"dva_opt") # best = 8629
##povprecje(10,berlin52,15,100,"dva_opt") # best = 10464

# tri_opt

##povprecje(10,berlin52,3,100,"tri_opt") # best = 7616
##povprecje(10,berlin52,5,100,"tri_opt") # best = 7684
##povprecje(10,berlin52,10,100,"tri_opt") # best = 7735
##povprecje(10,berlin52,15,100,"tri_opt") # best = 8705

# st70 velikosti 70x70
# ponovitve = 10, iter = 100
# 675 je znana optimalna rešitev

# dva_opt

##povprecje(10,st70,3,100,"dva_opt") # best = 714
##povprecje(10,st70,5,100,"dva_opt") # best = 888
##povprecje(10,st70,10,100,"dva_opt") # best = 1211
##povprecje(10,st70,15,100,"dva_opt") # best = 1386

# tri_opt

##povprecje(10,st70,3,100,"tri_opt") # best = 684
##povprecje(10,st70,5,100,"tri_opt") # best = 754
##povprecje(10,st70,10,100,"tri_opt") # best = 878
##povprecje(10,st70,15,100,"tri_opt") # best = 941


# kroA100 velikosti 100x100
# ponovitve = 10, iter = 100
# 21282 je znana optimalna rešitev

# dva_opt

##povprecje(10,kroA100,3,100,"dva_opt") # best = 37162
##povprecje(10,kroA100,5,100,"dva_opt") # best = 54119 
##povprecje(10,kroA100,10,100,"dva_opt") # best = 74951 
##povprecje(10,kroA100,15,100,"dva_opt") # best = 74462 

# tri_opt

##povprecje(10,kroA100,3,100,"tri_opt") # best = 22917
##povprecje(10,kroA100,5,100,"tri_opt") # best = 26938
##povprecje(10,kroA100,10,100,"tri_opt") # best = 41953
##povprecje(10,kroA100,15,100,"tri_opt") # best = 46026



# primerjava s skupino 7
# za grafe ulysses22, berlin52 in kroA100

# ulysses22
# GRASP: 7013
# genetski: 7112

# berlin52
# GRASP: 7692
# genetski: 8737

# kroA100
# GRASP: 21761
# genetski: 36408


# iter = 1000
# 2-opt

##povprecje(10,swiss42,3,1000,"dva_opt") # best = 1273
##povprecje(10,swiss42,5,1000,"dva_opt") # best = 1273
##povprecje(10,swiss42,10,1000,"dva_opt") # best = 1273
##povprecje(10,swiss42,15,1000,"dva_opt") # best = 1273
##povprecje(10,swiss42,30,1000,"dva_opt") # best = 1273

# vedno vrne optimalen rezultat 1273, neodvisno od parametra alfa

##povprecje(10,berlin52,3,1000,"dva_opt") # best = 7544
##povprecje(10,berlin52,5,1000,"dva_opt") # best = 7544
##povprecje(10,berlin52,10,1000,"dva_opt") # best = 7544
##povprecje(10,berlin52,15,1000,"dva_opt") # best = 7544
##povprecje(10,berlin52,30,1000,"dva_opt") # best = 7560

##povprecje(10,st70,3,1000,"dva_opt") # best = 678
##povprecje(10,st70,5,1000,"dva_opt") # best = 685
##povprecje(10,st70,10,1000,"dva_opt") # best = 678
##povprecje(10,st70,15,1000,"dva_opt") # best = 682
##povprecje(10,st70,30,1000,"dva_opt") # best = 685

##povprecje(10,kroA100,3,1000,"dva_opt") # best = 21381
##povprecje(10,kroA100,5,1000,"dva_opt") # best = 21709
##povprecje(10,kroA100,10,1000,"dva_opt") # best = 21642
##povprecje(10,kroA100,15,1000,"dva_opt") # best = 22009
##povprecje(10,kroA100,30,1000,"dva_opt") # best = 24275


#[7544.365901904088, 1, 22, 31, 18, 3, 17, 21, 42, 7, 2, 30, 23, 20, 50,
# 29, 16, 46, 44, 34, 35, 36, 39, 40, 37, 38, 48, 24, 5,
# 15, 6, 4, 25, 12, 28, 27, 26, 47, 13, 14, 52, 11, 51, 33, 43, 10, 9, 8, 41, 19, 45, 32, 49]

#print(povprecje(100,st70,3,1000,"dva_opt"))
 #[682.1505924549166, 1, 23, 16, 47, 37, 58, 50, 51, 56, 65, 64, 11, 67, 48, 54, 62, 33, 34, 21, 12, 60,
 # 52, 10, 5, 53, 6, 41, 43, 17, 9, 61, 39, 25, 45, 40, 46, 27, 68, 44, 30, 20,
 # 14, 28, 49, 55, 26, 8, 3, 32, 42, 18, 4, 2, 7, 19, 24, 15, 57, 63, 66, 22, 59, 38, 31, 69, 35, 70, 13, 29, 36]

#[678.9886291554706, 1, 36, 23, 13, 29, 70, 35, 69, 31,
 #                                        38, 59, 22, 66, 63, 57, 15, 24, 19, 7, 2, 4, 18, 42, 32, 3, 8, 26, 55, 49, 28, 14, 20, 30, 44, 68, 27, 46, 45, 25, 39, 61, 40, 9, 17, 43,
 #                                        41, 6, 53, 5, 10, 52, 60, 12, 21, 34, 33, 62, 54, 48, 67, 56, 11, 64, 65, 51, 50, 58, 37, 47, 16]

#(21381.84422089123, 21381.84422089123, [21381.84422089123, 1, 93, 28, 67, 58, 61, 51, 25, 81, 69, 64, 40, 54, 2, 44, 50, 73, 68, 85, 39, 82, 95,
#                                        13, 76, 33, 37, 5, 52, 78, 96, 30, 48, 100, 41, 71, 14, 3, 43, 46, 29, 34, 83, 55, 7, 9, 87, 57, 20, 12,
#                                        27, 86, 35, 62, 60, 77, 23, 98, 91, 45, 32, 11, 15, 17, 59, 74, 21, 72, 47, 63, 6, 49, 90,
#                                        10, 84, 36, 99, 38, 24, 18, 79, 53, 88, 16, 94, 22, 70, 66, 26, 65, 4, 19, 75, 97, 56, 80, 31, 89, 42, 8, 92])

