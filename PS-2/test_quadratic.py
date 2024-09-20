import numpy as np
import quadratic
def test_quadratic1():
    # Check the case from the problem
    x1, x2 = quadratic.quadratic(a=0.001, b=1000., c=0.001)
    assert (np.abs(x1 - (- 1.e-6)) < 1.e-10)
    assert (np.abs(x2 - (- 0.999999999999e+6)) < 1.e-10)
    
def test_quadratic2():
    # Check a related case to the problem
    x1, x2 = quadratic.quadratic(a=0.001, b=-1000., c=0.001)
    assert (np.abs(x2 - (1.e-6)) < 1.e-10)
    assert (np.abs(x1 - (0.999999999999e+6)) < 1.e-10)