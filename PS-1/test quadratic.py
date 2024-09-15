import pytest
import numpy as np
import quadratic
def test_quadratic():
    # Check the case from the problem
    x1, x2 = quadratic.quadratic(a=0.001, b=1000., c=0.001)
    assert (np.abs(x1 - (- 1.e-6)) < 1.e-10)
    assert (np.abs(x2 - (- 0.999999999999e+6)) < 1.e-10)
    # Check a related case to the problem
    x1, x2 = quadratic.quadratic(a=0.001, b=-1000., c=0.001)


