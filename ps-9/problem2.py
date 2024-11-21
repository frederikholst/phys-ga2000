import matplotlib.pyplot as plt
import numpy as np

## Constants
C=47
rho=1.22
v0=100
R=0.08
theta=30
g=9.87


def dxdot(xdot,ydot,m):
    factor=np.pi*R**2*rho*C/(2*m)
    return - factor*xdot*np.sqrt(xdot**2+ydot**2)

def dydot(xdot,ydot,m):
    factor=np.pi*R**2*rho*C/(2*m)
    return - g-factor*ydot*np.sqrt(xdot**2+ydot**2)

def Solver(m=1,mass=False):
    t0=0.0
    ydot=v0*np.sin(np.radians(theta))
    x=0.0
    t1=5
    xdot=v0*np.cos(np.radians(theta))

    N_steps=1000
    Deltat=(t1-t0)/N_steps  # Size of a single step
    y=0.0
    tpoints=np.arange(t0,t1,Deltat)
    xpoints=[]
    ypoints=[]
    xdotpoints=[]
    ydotpoints=[]
    # We first update y, then x:
    for t in tpoints:
        ydotpoints.append(ydot)
        ydot+=Deltat*dydot(xdot,ydot,m)
        ypoints.append(y)
        y+=Deltat*ydot

        xdotpoints.append(xdot)
        xdot+=Deltat*dxdot(xdot,ydot,m)
        xpoints.append(x)
        x+=Deltat*xdot
        if y<0:
            break
    if mass==True:
        return x
    else:
        return xpoints, ypoints,x
xpoints,ypoints,x=Solver()
plt.plot(xpoints,ypoints,".",label="Canonball")
plt.legend()
plt.xlabel("Horisontal distance [meters]")
plt.ylabel("Vertical distance [meters] ")

plt.savefig("cannon.png")
plt.clf()

### PART B ### 
mass_series=np.linspace(0.5,2,100)
distance_series=[Solver(m,mass=True) for m in mass_series]

plt.plot(mass_series,distance_series,".",label="Distance travelled for cannonballs")
plt.legend()
plt.ylabel("Horisontal distance travelled [meters]")
plt.xlabel("Cannonball mass [kg] ")
plt.savefig("mass.png")
plt.show()
