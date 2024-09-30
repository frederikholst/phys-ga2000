import numpy as np
import matplotlib.pyplot as plt

def gaussian_quadrature(f, a, b, n,a0): 
    """
    A function that computes the integral of a function f, from a to b with n points. 
    a0 is the upper limit 
    """
    # Gauss-Legendre nodes and weights for the interval [-1, 1]:
    roots, weights = np.polynomial.legendre.leggauss(n)
    
    # Transform roots from [-1, 1] to [a, b]:
    roots = (b-a)/2*roots+(b+a)/2
    
    # Scaled weights for the new interval [a, b]:
    w_scaled = (b-a)/2*weights
    
    integral = np.sum(w_scaled * f(roots,a0))
    
    return integral
def integrand(x,a0):
    return 1/(a0**4-x**4)

def T(a0):
    return np.sqrt(8)*gaussian_quadrature(integrand,0,a0,20,a0)

a_series=np.arange(0.1,2,0.01)

T_series=[T(a0) for a0 in a_series]

plt.plot(a_series,T_series,".")
plt.xlabel("Amplitude [A.U.]")
plt.ylabel("Period [A.U.]")
plt.savefig("Periods.png")
