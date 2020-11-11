#calcul delta
#variable A , B , C , delta , x1 , x2 , x ,

#equation : ax+bx+c=0  delta > 0 : deux solutions
#equation : ax+bx+c=0  delta = 0 : uni solution
#equation : ax+bx+c=0  delta < 0 : null makhadmch f l complexe normalement deux solutions
from math import *

print('salamo3alikom ikhwane britiw t calculiw delta mar7ba bikom')
print("dakhlo layrdi 3likom A ET B ET C ")
print("Tel que Ax²+Bx+C=0")

A=input('A=') # On rentre la valeur de A
B=input('B=') # On rentre la valeur de B
C=input('C=') # On rentre la valeur de C

delta=int(B)*int(B)-4*int(A)*int(C)

print ("Delta=",delta)


if delta <0:
        print ("Pas de solutions") #  delta  négatif, makaynch solution makhadaminch f complex
        print("delta  négatif, makaynch solution ")
if delta == 0:
            print("Une solution")  #  delta  égale  0,   solution Wahda X
            x = int(-B) / int(2) * int(A)  # Calcul de X1
            print("X=", x)  #  la solution
if delta > 0:
                print("deux solutions ")  # delta  seperieur  0, 2 solutions
                x1 = (int(B) - sqrt(int(delta))) / int(2) * int(A)  # Calcul de X1
                x2 = (int(B) + sqrt(int(delta))) / int(2) * int(A)
                print("X1=", x1 ,"ET","x2=" , x2)  # la solution



