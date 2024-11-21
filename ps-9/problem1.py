import numpy as np
import matplotlib.pyplot as plt

# We define the derivatives as functions in the same style as that of example 8.1 in Newman:


### PART A ###
def dx(y):
    return y

def dy(x,anhar):
    return -np.power(x,anhar)

def Solver(x=1.0,anhar=1,phasespace=False,mu=0,t1=50):
    t0=0.0

    N_steps=1000
    Deltat=(t1-t0)/N_steps  # Size of a single step
    y=0.0
    tpoints=np.arange(t0,t1,Deltat)
    xpoints=[]
    ypoints=[]
    # We first update y, then x:
    for t in tpoints:
        ypoints.append(y)
        y+=Deltat*(dy(x,anhar)+mu*(1-x**2)*y)

        xpoints.append(x)
        x+=Deltat*dx(y)
    if phasespace:
        return xpoints, ypoints
    else:
        return xpoints, tpoints

xpoints,tpoints=Solver()
plt.plot(tpoints,xpoints,".",label="SHO with A=1")
plt.xlabel("Amplitude [A.U.]")
plt.ylabel("Time [A.U.]")
plt.legend()


### PART B ###

xpoints,tpoints=Solver(2,3)
plt.plot(tpoints,xpoints,".",label="SHO with A=2")
plt.savefig("SHO1.png")
plt.clf()


### PART C ###

xpoints2,tpoints=Solver(2,3)
xpoints1,tpoints=Solver(1,3)
xpoints05,tpoints=Solver(0.5,3)

plt.plot(tpoints,xpoints1,".",label="AHO with A=1")
plt.plot(tpoints,xpoints2,".",label="AHO with A=2")
plt.plot(tpoints,xpoints05,".",label="AHO with A=0.5")
plt.legend()
plt.xlabel("Amplitude [A.U.]")
plt.ylabel("Time [A.U.]")
plt.savefig("AHO.png")
plt.clf()


### PART D ###

xpoints,ypoints,=Solver(1,1,True)


plt.plot(xpoints,ypoints,".",label="Phase space of SHO with A=1")

plt.legend()
plt.ylabel("y=dx/dt [A.U.]")
plt.xlabel("x [A.U.]")
plt.savefig("phase.png")
plt.clf()


### PART E ###


xpoints,ypoints,=Solver(1,1,True,mu=1,t1=20)
xpoints2,ypoints2,=Solver(1,1,True,mu=2,t1=20)
xpoints4,ypoints4,=Solver(1,1,True,mu=4,t1=20)



plt.plot(xpoints,ypoints,".",label="mu=1")
plt.plot(xpoints2,ypoints2,".",label="mu=2")
plt.plot(xpoints4,ypoints4,".",label="mu=4")

plt.legend()
plt.ylabel("y=dx/dt [A.U.]")
plt.xlabel("x [A.U.]")
plt.savefig("Pol.png")

