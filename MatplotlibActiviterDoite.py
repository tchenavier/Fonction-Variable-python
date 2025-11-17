from pylab import *
xlim(0,50)
ylim(0,50)

for i in range (1,31):#courbe 1
    x=5+i
    y=5+i
    i+1
    plot(x,y,'*r')
i=0

for i in range (1,31): #courbe 2
    x=3+i
    y=2+i
    i+0.5
    plot(x,y,'*b')
i=0

for i in range (1,31):#courbe 3
    x=0+i
    y=1+i
    i+1
    plot(x,y,'*g')
show()