import numpy as np
import matplotlib.pyplot as plt
def half_life_p(T):
    """
    Input: Half-life in seconds (Float)
    Output: The prob. of decaying within one second (Float)
    """
    return 1-2**(-1/T)

Bi_N=10000 # Number of Bi atoms
Ti_N=0
Pb_N=0
Bi209_N=0


p_Ti=0.0209 
Bi_T=46*60 # Decay in seconds
Pb_T=3.3*60 # Decay in seconds
Ti_T=2.2*60 # Decay in seconds

#Probabilites that the nuclei will decay in the time interval of 1 sec.
p_Bi_T=half_life_p(Bi_T) 
p_Pb_T=half_life_p(Pb_T)
p_Ti_T=half_life_p(Ti_T)

tmax=20000
Ti_series=[]
Pb_series=[]
Bi_series=[]
Bi209_series=[]

tpoints=np.arange(0.,tmax)

t=0
while True:
    
    Ti_series.append(Ti_N)
    Pb_series.append(Pb_N)
    Bi_series.append(Bi_N)
    Bi209_series.append(Bi209_N)
    for i in range(Pb_N):
        if np.random.rand()<p_Pb_T:
            Pb_N-=1
            Bi209_N+=1
    for i in range(Ti_N):
        if np.random.rand()<p_Ti_T:
            Ti_N-=1
            Pb_N+=1
    for i in range(Bi_N):
        if np.random.rand()<p_Bi_T:
            Bi_N-=1
            if np.random.rand()<p_Ti:
                Ti_N+=1
            else:
                Pb_N+=1
    t+=1
    if t==tmax:
        break
    

plt.plot(tpoints,Pb_series,label="Pb")
plt.plot(tpoints,Ti_series,label="Ti")
plt.plot(tpoints,Bi209_series,label="Bi-209")
plt.plot(tpoints,Bi_series,label="Bi-213")
plt.ylabel("Number of nuclei (N)")
plt.xlabel("Time (s)")
plt.legend()
plt.grid()
plt.savefig("Decay.png")



