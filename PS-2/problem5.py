import numpy as np
def quadratic_solver1(a,b,c):
    """Solves quadratic equations of the form:
    ax^2+bx+c=0"""
    return [(-b+np.sqrt(b**2-4*a*c))/(2*a),(-b-np.sqrt(b**2-4*a*c))/(2*a)]

def quadratic_solver2(a,b,c):
    """Solves quadratic equations of the form:
    ax^2+bx+c=0 with a variation to the standard formula"""
    return [2*c/(-b-np.sqrt(b**2-4*a*c)),2*c/(-b+np.sqrt(b**2-4*a*c))]
x_solutions1=quadratic_solver1(0.001,1000,0.001)
x_solutions2=quadratic_solver2(0.001,1000,0.001)
print("Roots for the first solver: ",x_solutions1[0],x_solutions1[1])
print("Roots for the second solver: ", x_solutions2[0],x_solutions2[1])