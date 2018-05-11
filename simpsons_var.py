import numpy
from matplotlib import pyplot as plt

def simpvar(x,fun):
    xmid=0.5*(x[:-1]+x[1:])
    y=fun(x)
    ymid=fun(xmid)
    tot=0
    for i in range(len(xmid)):
        myarea=4*ymid[i]+y[i]+y[i+1]
        dx=x[i+1]-x[i]
        myarea=myarea*dx/6.
        tot+= myarea
    return tot

def lorentz(x):
    y=1.0/(1+x**2)
    return y

x=numpy.linspace(0,numpy.pi,50)
tot=simpvar(x,numpy.sin)
print tot,tot-2

x=numpy.linspace(-10,10,39)
tot_fine=simpvar(x,lorentz)
pred=numpy.arctan(x.max())-numpy.arctan(x.min())
print x[1]-x[0],tot_fine,pred,(tot_fine-pred)/pred

x1=numpy.arange(-10,-2)
x2=numpy.arange(-2,2,0.1)
x3=numpy.arange(2,11)
xx=numpy.concatenate((x1,x2,x3))
tot2=simpvar(xx,lorentz)
print len(xx), len(x), tot2,(tot2-pred)/pred
