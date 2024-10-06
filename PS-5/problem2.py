import numpy as np
import matplotlib.pyplot as plt

## PART A

def gamma_int(x,a):
    """The integrand of the gamma function"""
    return x**(a-1)*np.exp(-x)

x_series=np.arange(0,5,0.01)
a_series=[2,3,4]
for a in a_series:
    gamma_int_series=[gamma_int(x,a) for x in x_series]
    plt.plot(x_series,gamma_int_series,label=f"Integrand of Gamma with a={a}")
plt.ylabel("Integrand [A.U.]")
plt.xlabel("x [A.U.]")
plt.legend()
plt.savefig("integrand_plot.png")


## Part E:
## We rewrite the gamma integrand and carry out the integration using Guass-Quadratures.

def gaussian_quadrature(f, a_order,a=0, b=1,n=50):
    """
    A function that computes the integral of a function f, from a to b with n points. 
    
    """
    # Gauss-Legendre nodes and weights for the interval [-1, 1]:
    roots, weights = np.polynomial.legendre.leggauss(n)
    
    # Transform roots from [-1, 1] to [a, b]:
    roots = (b-a)/2*roots+(b+a)/2
    
    # Scaled weights for the new interval [a, b]:
    w_scaled = (b-a)/2*weights
    
    integral = np.sum(w_scaled * f(roots,a_order))
    
    return integral

def Gamma_integrand_cvar(z,a):
    """The integrand of the Gamma function with changed variables."""
    x=z*(a-1)/(1-z)
    return (a-1)/(1-z)**2*np.exp((a-1)*np.log(x)-x)

gam32=gaussian_quadrature(Gamma_integrand_cvar,3/2)
print("Gamma(3/2): ",gam32)
print("Gamma(3): ",gaussian_quadrature(Gamma_integrand_cvar,3))
print("Gamma(6): ",gaussian_quadrature(Gamma_integrand_cvar,6))
print("Gamma(10)",gaussian_quadrature(Gamma_integrand_cvar,10))








