xA = float(input ("ordonner de A\n"))#pour les entrée utilisateur
xB = float(input ("ordonner de B\n"))
yA = float(input ("abscisse de A\n"))
yB = float(input ("abscisse de B\n"))

a=(yB-yA)/(xB-xA)
b=yA-a*xA

print("y=",a,"x+",b) #imprimer les réponse a l'ecrant