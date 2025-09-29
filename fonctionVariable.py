xA = float(input ("ordonner de A"))
xB = float(input ("ordonner de B"))
yA = float(input ("abscisse de A"))
yB = float(input ("abscisse de B"))

a=(yB-yA)/(xB-xA)
b=yA-a*xA

Print("y=",a,"x+",b)