import numpy as np
import matplotlib.pyplot as plt
def Gaussian(x):
    """
    Input: float
    Ouput: Value of Gaussian at that x-value
    """
    sig=2
    
    return 1/(sig*np.sqrt(2*np.pi))*np.exp(-(x+3)**2/(2*sig**2))
y_values=np.array([])
x_values=np.arange(-10,10)
for i in x_values:
    y_values=np.append(y_values,Gaussian(i))

plt.plot(x_values,y_values)
plt.savefig("gaussian.png")