import numpy as np
import matplotlib.pyplot as plt
from dcst import dst,idst
from matplotlib.animation import FuncAnimation

m=9.109e-31 #Mass of electron in kg
Len=1e-8 #Length of box in m
x0=Len/2
sig=1e-10
kap=5e10
N=1000
x_series=np.linspace(0,Len,N)
hbar=1.054e-34 # hbar in Js
psi0=np.array([np.exp(-(x-x0)**2/(2*sig**2))*np.exp(-1j*kap*x) for x in x_series])

alpha_k=dst(np.real(psi0))
eta_k=dst(np.imag(psi0))
k_array=np.arange(1,N-1)

def RealPsi_n(t,n):
    
    sum_k=0
    for i in range(len(k_array)):
        omega_k=np.pi**2*hbar*k_array[i]**2/(2*m*Len**2)
        sum_k+=(alpha_k[i]*np.cos(omega_k*t)-eta_k[i]*np.sin(omega_k*t))*np.sin(np.pi*k_array[i]*n/N)
    return 1/N*sum_k

def Psi_n_func(t):
    return np.array([RealPsi_n(t,n) for n in np.arange(N)])


t=1e-16
Psi_n_array=Psi_n_func(t)
#Psi_inverted=idst(Psi_n_array)


#plt.plot(x_series,Psi_n_array,".",label="non-inverted")
#plt.plot(x_series,Psi_inverted,label="Inverted")
plt.plot(x_series,Psi_n_array,label="Spectral method solution at time t=1e-16")
plt.xlabel("Distance, [m]")
plt.ylabel("Amplitude [A.U.]")
plt.legend()
plt.xlim(0.4*Len,0.7*Len)
plt.savefig("Spectral Method")
plt.clf()

## We now setup the animation

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Spectral Wavefunction")
ax.set_xlim(0, Len)
ax.set_ylim(-0.8,0.8)
ax.set_xlabel("Distance [m]")
ax.set_ylabel("Amplitude [A.U.]")
ax.legend()

Delta_t=1e-17
t_stop=1e-15



def init():
    line.set_data([], [])
    return line,
psi_list=[Psi_n_func(t) for t in np.arange(0,t_stop,Delta_t)]
    
def update(frame):
    line.set_data(x_series, np.real(psi_list[frame]))  
    return line,


anim = FuncAnimation(fig, update, frames=len(psi_list), init_func=init, blit=True)

anim.save("spectral_animation.mp4", fps=10)

