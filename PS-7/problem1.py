import numpy as np
import matplotlib.pyplot as plt

#Defining constants:

M0=5.974e24 # Earth's mass
m0=7.348e22 # Moon's mass
R0=3.844e8

acc =1e-15


def lagrange(r,m=1):
    # Computes the polynomial with m'=1:
    return 1/r**2-m/(1-r)**2-r

def derivative(r,m=1):
    #Computes the derivative of the polynomial:
    return -2/r**3-2*m/(1-r)**3-1

def Newton(r0,m):

    r=r0
    delta=1
    while abs(delta)>acc:
        delta=lagrange(r,m)/derivative(r,m)
        r-= delta
    return r

print("The lagrange point for Earth and moon is at: ", Newton(0.80,m0/M0)*R0)

m_sun=1.989e30 # mass of the sun
R0_sun=1.496e11 # distance between earth and sun
print("The lagrange point for the Earth and sun is at", Newton(0.80,M0/m_sun)*R0_sun/1e9, "million kilometers")

m_jupyter=1.898e27


print("The lagrange point for the jupyter mass planet at earth's distance and sun is at", Newton(0.80,m_jupyter/m_sun)*R0_sun/1e9, "million kilometers")