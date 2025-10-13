xA = float(input ("ordonner de A"))#pour les entrée utilisateur
xB = float(input ("ordonner de B"))
yA = float(input ("abscisse de A"))
yB = float(input ("abscisse de B"))

a=(yB-yA)/(xB-xA)
b=yA-a*xA

print("y=",a,"x+",b) #imprimer les réponse a l'ecrant