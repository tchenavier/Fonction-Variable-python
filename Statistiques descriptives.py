from math import *  # inutile pour le moment
from pylab import * # inutile pour le moment

Total = 0
Moyenne = 0.00
minimum = 552.129
maximum = 552.129
aout = [22, 22.6, 21.1, 21.9, 18.3, 18.7, 21.7, 21.1, 23.6, 27.4, 25.1, 24.9, 23.7, 28.9,  23.2, 26.1, 26.1, 29.8, 28.2, 28.7, 25.9, 26.7, 30.3, 25.2, 21.8, 22, 20.9, 20.7, 20.6, 19.5, 18.8]
sort(aout) #Permettant de ranger les valeurs du tableau dans l'ordre  croissant
taille = len(aout) # récuper la taille du tableau 
for i in range (0,taille):
    e = float(input ("Temprerature\n"))
    Total = Total + e
    #partie pour les minimum et le maximum
    if ( e< minimum or minimum == 552.129):
        minimum = e
    if ( e > maximum or maximum == 552.129):
        maximum = e
Etendue = maximum-minimum

Moyenne = Total/31

print(Moyenne)