import numpy as np
import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt

def ftanh(x):
    return 1+1/2*np.tanh(2*x)

def cent_dev_tanh(x,h):
    """Central difference derivative of 1+1/2tanh funciton.
    Parameters:
    x value, float

    return:
    derivative, float
    """
    f1=ftanh(x+h/2)
    f2=ftanh(x-h/2)
    return (f1-f2)/h


h=0.01
x_series=np.arange(-2,2,h)
cent_dev_series=[cent_dev_tanh(x,h=0.01) for x in x_series]
analytic_series=[1/(np.cosh(2*x)**2) for x in x_series]



plt.plot(x_series,cent_dev_series,"o",alpha=0.3,label="Central difference derivative")
plt.plot(x_series,analytic_series,label="Analytic derivative")
plt.legend()
plt.ylabel("Derivative, [unit: tanh(x)/x]")
plt.xlabel("x-values, [A.U.]")
plt.grid()
plt.savefig("problem1.png")
plt.clf()


## We now repeat the computation, but now using JAX instead:
def jax_tanh(x):
    return 1+1/2*jnp.tanh(2*x)

jax_derivative=jax.grad(jax_tanh)
plt.plot(x_series,[jax_derivative(x) for x in x_series],"o",alpha=0.2,label="Jax derivative")
plt.plot(x_series,analytic_series,label="Analytic derivative")
plt.legend()
plt.ylabel("Derivative, [unit: tanh(x)/x]")
plt.xlabel("x-values, [A.U.]")
plt.grid()
plt.savefig("Jax.png")
plt.clf()

## Let's plot the resiudals of JAX derivative:
jax_derivatives=[jax_derivative(x) for x in x_series]
residuals=[]
for i,dev_j in enumerate(jax_derivatives):
    residuals.append(analytic_series[i]-dev_j)
plt.plot(x_series,residuals,"o",alpha=0.2,label="Jax derivative")
plt.legend()
plt.ylabel("Residuals, [A.U.]")
plt.xlabel("x-values, [A.U.]")
plt.grid()
plt.savefig("Jax_res.png")


