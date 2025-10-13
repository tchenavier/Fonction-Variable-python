from math import * #importe la fonction sqrt et les autre fonction qui sont dans la librairi math

a = float(input ("La valeur de a\n"))
b = float(input ("La valeur de b\n"))
c = float(input ("La valeur de c\n"))

d=b**2-4*a*c
if (a!=0):
    if (d==0):   #condition pour si d=0 donc une seul racine
        X=-b/(2*a)
        print("Une seule racinne réelle qui est ",X)
        #valeur teste a=3 b=-12 c=12 x=2
    elif (d>0):  #https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7168878-controlez-le-deroulement-de-votre-programme-avec-des-conditions
        r= sqrt(d) #racine carré
        X1=(-b-r)/(2*a)
        X2=(-b+r)/(2*a)
        print("La premiere racine ",X1,"\nla deuxieme racine ",X2) #affiche les deux racine
        #valeur teste a=2; b=4;c=-6 x=-3 x2=1
    else :
        print("Pas de racine réelle.\n")
        # valeur teste a=3 b=-2 c=1
else :
    print("La valeur de a n'est pas valable.\n")