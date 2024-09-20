import numpy as np
import timeit
import matplotlib.pyplot as plt

def Matrix_Multi_loops(N=100):
    C=np.zeros([N,N],float)
    A=np.random.random((N,N))
    B=np.random.random((N,N))
    for i in range(N):
        for j in range (N):
            for k in range (N):
                C[i,j]+=A[i,k]*B[k,j]

def Matrix_Multi_dot(N=100):
    A=np.random.random((N,N))
    B=np.random.random((N,N))
    return(np.dot(A,B))
        

comp_time_loops=np.array([])
comp_time_dot=np.array([])
N_list=np.array([10,30,40,50,60,70,80,90,100])

for i in N_list:
    runtime=timeit.timeit(lambda: Matrix_Multi_loops(i),number=1)
    comp_time_loops=np.append(comp_time_loops,runtime)

for i in N_list:
    runtime=timeit.timeit(lambda: Matrix_Multi_dot(i),number=1)
    comp_time_dot=np.append(comp_time_dot,runtime)

a=(N_list[-1]**3)/comp_time_loops[-1]
print("This is a",a)
N_cube=N_list**3/a
plt.plot(N_list,N_cube,label="N^3")
plt.plot(N_list,comp_time_loops,label="Computation time with loops")
plt.plot(N_list,comp_time_dot,label="Computation time using np.dot")
plt.legend()
plt.yscale("log")
plt.grid()
plt.ylabel("Computation time [s]")
plt.xlabel("Matrix size (NxN)")
plt.savefig("loops_comp.png")


print(comp_time_loops)