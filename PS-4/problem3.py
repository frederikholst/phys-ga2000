import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

def psi(x,n):
    return 1/np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi))*np.exp(-x**2/2)*H(x,n)


def H(x,n):
    
    if n==0:
        return 1
    if n==1:
        return 2*x
    else:
        return 2*x*H(x,n-1)-2*(n-1)*H(x,n-2)
    
n_values=np.array([0,1,2,3])
x_series=np.arange(-4,4,0.1)
waveamplitudes=[np.array([]),np.array([]),np.array([]),np.array([])]

for i,n in enumerate(n_values):
    for x in x_series:
        waveamplitudes[i]=np.append(waveamplitudes[i],psi(x,n))
    plt.plot(x_series,waveamplitudes[i],label=f"n={n}",)


plt.xlabel("x coordinate")
plt.ylabel("Wavefunction amplitude")
plt.legend()
plt.savefig("Wavefunctions_n1-3.png")
plt.clf()
n=31
x_series2=np.arange(-10,10,0.01)
waveamplitude=psi(x_series2,n)
plt.plot(x_series2,waveamplitude,label="n=30")
plt.xlabel("x coordinate")
plt.ylabel("Wavefunction amplitude")
plt.legend()
plt.savefig("Wavefunctions_n30.png")
        

def gaussian_quadrature(f, a, b, n):
    """
    A function that computes the integral of a function f, from a to b with n points. 
    
    """
    # Gauss-Legendre nodes and weights for the interval [-1, 1]:
    roots, weights = np.polynomial.legendre.leggauss(n)
    
    # Transform nodes from [-1, 1] to [a, b]:
    roots = (b-a)/2*roots+(b+a)/2
    # Scale the weights for the new interval [a, b]:
    w = (b-a)/2*weights
    
    integral = np.sum(w * f(roots,5))
    
    return integral


def wave_pos(x,n):
    return x**2*psi(x,n)**2


sample_points=100
a=-10
b=10
mean_square_position= gaussian_quadrature(wave_pos,a,b,sample_points)
print("The mean square using Gaussian quadrature",mean_square_position**(0.5))
    
## We now repeat the computation with Gauss-Hermite quadrature
def Hermite_quadrature(f, n):
    """
    A function that computes the integral of a function f, from -inf to inf using Gauss-Hermite quadrature. 
    
    """
    
    roots, weights = scipy.special.roots_hermite(n, mu=False)
    
    
    hermite_integral = np.sum(weights * f(roots,5)*np.exp(roots**2)) # Since f should only include the integrand without the exponent, we compensate by factoring it in here. 
    
    return hermite_integral




sample_points=9
mean_square_position= Hermite_quadrature(wave_pos,sample_points)
print("The mean square using Gaus-Hermite quadrature is",mean_square_position**(0.5))

print("The difference between the Hermite_quadrature result and the theoretical is: ",2.345207879911714-mean_square_position**(0.5))