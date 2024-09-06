import numpy as np
import matplotlib.pyplot as plt

def Gaussian(x):
    """
    Input: float
    Ouput: Value of Gaussian at that x-value
    """
    sig=3
    
    return 1/(sig*np.sqrt(2*np.pi))*np.exp(-(x**2)/(2*sig**2))
y_values=np.array([])
x_values=np.arange(-10,11,0.1)
for i in x_values:
    y_values=np.append(y_values,Gaussian(i))

plt.plot(x_values,y_values)
plt.title("Gaussian Distribution")
plt.ylabel("y")
plt.xlabel("x")
plt.savefig("phys-ga2000\\PS-1\\gaussian.png")