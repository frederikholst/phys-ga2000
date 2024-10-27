import numpy as np


# First we define the three different iteration methods, parabolic, secant and bisection that will be used in Brent's minimazation method:

def parabolic_step(f, a, b, c):
    # Fit a parabola through a, b, and c 
    fa,fb,fc=f(a),f(b),f(c)
    A=(a*(fc-fb)+b*(fa-fc)+c*(fb-fa))/((a-b)*(a-c)*(b-c))
    B=(a**2*(fb-fc)+b**2*(fc-fa)+c**2*(fa-fb))/((a-b)*(a-c)*(b-c))
    if A==0:
        return b  # In case of division with zero, return midpoint
    return -B/(2*A)

def secant_step(f, b, c):
    # Perform secant method to find root of the derivative
    fb,fc=f(b),f(c)
    if fb == fc:
        return b  # Avoid division by zero
    return b-fb*(b-c)/(fb-fc)  

def bisection_step(a,c):
    # Return midpoint
    return 0.5*(a+c)


def brent(f,a0,b0,c0,tol=1e-4):
    a,b,c=a0,b0,c0
    b_old = b + 10. * tol #Ensures that at least one iteration will be performed. 

    while (np.abs(b_old-b)>tol):
        b_old=b
        print("b_old=",b_old)

        # First we try the Secant method. If b and c are sufficiently far apart, do secant method, otherwise do nothing:
        if np.abs(b-c)>tol:
                b_new=secant_step(f,b,c)
                print("Secant step")
        else: b_new=b


        # Parabolic method if three distinct points
        if (a != b) and (b != c) and (a != c):
            b_par=parabolic_step(f,a,b,c)
            if a < b_par < c: # If the new step from parabolic method doesn't fall outside of the range of a and c, continue:
                b_new = b_par
                print("Para step")
        

        # If everything else fails, we will resort to bisection:
        if not (a<b_new<c):
            b_new=bisection_step(a,c)
            print("bisection step")
        
        if f(b_new)<f(b):
            if b_new<b:
                c=b
            else:
                a=b
            
        else:
            if b_new<b:
                a=b_new
            else:
                c=b_new
        b=b_new
        print("b_new=",b_new)
        print("f(b_new)=",f(b_new))
        print("f(b)",f(b))
    return b

def exp_func(x):
    return (x-0.3)**2*np.exp(x)

print("The minimum of y(x) is found to be x_min = ", brent(exp_func,-0.5,0.1,1))



# We now compare with scipy:
from scipy.optimize import minimize
scipy_min=minimize(exp_func,0)
print("The scipy package computes the derivative to be",scipy_min.x, "making the fractional difference: ",1.-brent(exp_func, -0.5, 0.1, 1, tol=1e-6)/scipy_min.x) 