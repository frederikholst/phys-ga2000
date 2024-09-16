import matplotlib.pyplot as plt 
import numpy as np
N=2000
plane=np.zeros((N,N))
axis_arr=np.arange(-2,2,4/N)



for i in np.arange(len(axis_arr)):
    for h in np.arange(len(axis_arr)):
        c=axis_arr[i]+axis_arr[h]*1j
        k=0
        z=c
        while k < 100:
            z=z**2+c
            k+=1
            if np.absolute(z)>2:
                plane[i,h]=k
                break
        if np.absolute(z)<2:
            plane[i,h]=101


plt.figure(figsize=(10,10))
plt.imshow(plane,cmap=("jet"),extent=[-2, 2, -2, 2])

plt.xlabel("x")
plt.ylabel("y")

plt.colorbar()
plt.savefig("fractal.png")


