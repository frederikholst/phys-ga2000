import numpy as np
import matplotlib.pyplot as plt
Ti_T=3.053*60 # Half life in seconds
def non_uniform(z):
    """Inputs the 1D, np.array of uniform, random floats, z and returns a non uniform array, x"""
    mu=np.log(2)/Ti_T
    return -1/mu*np.log(1-z)


z_array=np.random.rand(1000)
x_array=non_uniform(z_array)
x_array_sort=np.sort(x_array)
tmax=2000
time=np.arange(0,tmax)

Nuclei_population_series=np.array([np.sum(x_array >t) for t in time])
plt.plot(time,Nuclei_population_series)
plt.ylabel("Population of atoms (N)")
plt.xlabel("Time (s)")
plt.legend()
plt.savefig("decay2")
