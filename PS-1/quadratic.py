import numpy as np
def quadratic(a,b,c):
    """Takes in a polynomial of second order and returns two roots. The solver will choose for each root the best solver, to avoid errors with subtraction of large, similar numbers."""
    d=np.sqrt(b**2-4*a*c)
    if d-b<0.01:
        return  [(-b-np.sqrt(b**2-4*a*c))/(2*a),2*c/(-b-np.sqrt(b**2-4*a*c))]
    else:
        return  [(-b+np.sqrt(b**2-4*a*c))/(2*a),2*c/(-b+np.sqrt(b**2-4*a*c))]


