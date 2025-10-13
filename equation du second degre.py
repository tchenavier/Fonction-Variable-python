from math import * #importe la fonction sqrt et les autre fonction qui sont dans la librairi math

a = float(input ("La valeur de a"))
b = float(input ("La valeur de b"))
c = float(input ("La valeur de c"))

d=b**2-4*a*c

if (d==0):   #condition pour si d=0 donc une seul racine
    X=-b/2*a
    print("La racinne est",X)
elif (d>0):  #https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7168878-controlez-le-deroulement-de-votre-programme-avec-des-conditions
    r= sqrt(d) #racine carré
    X1=b-r/2*a
    X2=b+r/2*a

    print("La premiere racine",X1,"la deuxieme racine",X2) #affiche les deux racine

print("Pas de racine réelle")