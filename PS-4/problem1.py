import numpy as np
from scipy.integrate import fixed_quad
import matplotlib.pyplot as plt


def debye(x):
    result=x**4*np.exp(x)/((np.exp(x)-1)**2)
    return result

theta_D=428 # debye temp. in Kelvin.

rho=6.022e28 # m^-3
Vol=1e-3 # m^3
kB=1.381e-23 # Boltzmann's constant in SI units

def gaussian_quadrature(f, a, b, n):
    """
    A function that computes the integral of a function f, from a to b with n points. 
    
    """
    # Gauss-Legendre nodes and weights for the interval [-1, 1]:
    roots, weights = np.polynomial.legendre.leggauss(n)
    
    # Transform roots from [-1, 1] to [a, b]:
    roots = (b-a)/2*roots+(b+a)/2
    
    # Scaled weights for the new interval [a, b]:
    w_scaled = (b-a)/2*weights
    
    integral = np.sum(w_scaled * f(roots))
    
    return integral
def cv_result(t,N=50):
    a=0
    b=theta_D/t
    integral=gaussian_quadrature(debye,a,b,N)
    return 9*Vol*kB*rho*(t/theta_D)**3*integral

print("The heat capacity for 50 sample points and T=50 is: ", cv_result(50))
T_series=np.arange(5,501,1)
cv_series=np.array([])
for t in T_series:
    cv_series=np.append(cv_series,cv_result(t))



plt.plot(T_series,cv_series,".")
plt.xlabel("Temperature [K]")
plt.ylabel("Heat capacity, Cv [J/K]")
plt.savefig("T_series.png")
plt.clf()


Sample_Numbers=np.arange(10,71,1)
t=5

integration_results=[]
for Num in Sample_Numbers:
    a=0
    b=theta_D/t
    integral=gaussian_quadrature(debye,a,b,Num)
    factor=9*Vol*kB*rho*(t/theta_D)**3
    integration_results.append(factor*integral)


plt.plot(Sample_Numbers,integration_results,".")
plt.xlabel("Sample size, N")
plt.ylabel("Computation result of Cv, [J/K]")
plt.savefig("Convergence.png")