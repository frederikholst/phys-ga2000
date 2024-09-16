import numpy as np
import timeit

L=100


timing_1 ="""
global M
M=0
for i in np.arange(-L,L+1):
    for j in np.arange(-L,L+1):
        for k in np.arange(-L,L+1):
            if (i+j+k) % 2==0:
                q=-1
            else:
                q=1
            if i**2+j**2+k**2!=0:
                M+=q/(np.sqrt(i**2+j**2+k**2))
            


"""

execution_time = timeit.timeit(timing_1, globals=globals(), number=1)
print("The Madelung constant computed using for-loops is:",M)
print("10 computations were done in ",execution_time, "seconds")

timing_2 ="""
global M
M=0
i, j, k = np.meshgrid(np.arange(-L, L+1), np.arange(-L, L+1), np.arange(-L, L+1))


r = np.sqrt(i**2 + j**2 + k**2)


r[L, L, L] = np.inf

# Essentially removing the singularity by setting 1/r to zero. 

charge_factor = (-1.)**(i + j + k)

M = np.sum(-charge_factor / r)

"""
execution_time2 = timeit.timeit(timing_2, globals=globals(), number=1)

print("The Madelung constant computed without for-loops is:",M)
print("10 computations were done in ",execution_time2, "seconds")