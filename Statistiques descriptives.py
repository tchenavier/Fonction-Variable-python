from math import *  # inutile pour le moment
from pylab import * # inutile pour le moment

Total = 0
Moyenne = 0.00
minimum = 552.129
maximum = 552.129
for i in range (1,31):
    e = float(input ("Temprerature\n"))
    Total = Total + e
    #partie pour les minimum et le maximum
    if ( e< minimum or minimum == 552.129):
        minimum = e
    if ( e > maximum or maximum == 552.129):
        maximum = e
        
Moyenne = Total/31
print(Moyenne)