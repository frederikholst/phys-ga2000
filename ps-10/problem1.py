import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m=9.109e-31 #Mass of electron in kg
Len=1e-8 #Length of box in m
sig=1e-10 # Width of Gaussian in m
kap=5e10 # Wavenumber in 1/m in
x0=Len/2 
N_samples=1000 # Number of spatial slices
a=Len/N_samples# Length of spatial step
h=1e-18 # Temporal step size
hbar=1.054e-34 # hbar in Js
a1=1+h*hbar*1j/(2*m*a**2)
a2=-1j*h*hbar/(4*m*a**2)
b1=1-h*1j*hbar/(2*m*a**2)
b2=h*1j*hbar/(4*m*a**2)
x_series=np.linspace(0,Len,N_samples)

psi0=np.array([np.exp(-(x-x0)**2/(2*sig**2))*np.exp(1j*kap*x) for x in x_series])

## To compute the first step we first find the vector, v:
v_vector=np.zeros_like(psi0)
for i,v in enumerate(v_vector[1:-1]):
    v_vector[i]=b1*psi0[i]+b2*(psi0[i+1]+psi0[i-1])

## Then we use the package from Newman online resources and compute x from Ax=v:

# Create the banded matrix

## Following the documentation from Newmans code, we construct the banded, compressed matrix: 
A_banded = np.zeros((3, N_samples),dtype=complex)  # For up=1, down=1
A_banded[1]=a1  # Main diagonal
A_banded[0,1:]=a2  # Upper diagonal
A_banded[2,:-1]=a2  # Lower diagonal
from banded import banded
psi1=banded(A_banded,v_vector,1,1)

plt.plot(x_series,np.real(psi0),".",label="Psi(t=0)")
plt.plot(x_series,np.real(psi1),label="Psi(t=h)")
plt.xlabel("Distance, [m]")
plt.ylabel("Amplitude [A.U.]")
plt.legend()
plt.xlim(0.4*Len,0.6*Len)
plt.savefig("One Step")
plt.clf()


## We now generalize this to take on many more time steps:
t=0
t_max=2000
psi_list=[psi0]
psi=np.copy(psi0)
while t<t_max*h:
    v_vector=np.zeros_like(psi0)
    for i,v in enumerate(v_vector[1:-1]):
        v_vector[i]=b1*psi[i]+b2*(psi[i+1]+psi[i-1])
    psi=banded(A_banded,v_vector,1,1)
    psi_list.append(psi)

    t+=h

for i in range(9):
    plt.plot(x_series,np.real(psi_list[int(t_max/10*i)]),label=f"Psi(t={100*i}h)"
    )
plt.legend()
plt.xlabel("Distance, [m]")
plt.ylabel("Amplitude [A.U.]")
plt.xlim(0.4*Len,Len)
plt.savefig("10 waves")
plt.clf()

## Now let's make the animation: 

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Wavefunction")
ax.set_xlim(0, Len)
ax.set_ylim(-1, 1)
ax.set_xlabel("Distance [m]")
ax.set_ylabel("Amplitude [A.U.]")
ax.legend()


def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x_series, np.real(psi_list[frame]))  
    return line,


anim = FuncAnimation(fig, update, frames=len(psi_list), init_func=init, blit=True)


anim.save("wavefunction_animation.mp4", fps=120)

# To display the animation

