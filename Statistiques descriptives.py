from math import *
from pylab import *

Total = 0
Moyenne = 0.00
for i in range (1,31):
    e = float(input ("Temprerature\n"))
    Total = Total + e

Moyenne = Total/31
print(Moyenne)