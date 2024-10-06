import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg

# We open the file and clean each line by removing the string elements:'|' and ' ':
with open('signal.txt', 'r') as file:
    lines = file.readlines()
cleaned_lines = [line.replace('|', ' ').strip() for line in lines[1:]]

data = np.loadtxt(cleaned_lines)

time = data[:,0]
t_range=time.max()
b = data[:,1] # Here b refers to the signal 
t=time/time.max() # Normalizes so that we don't deal with 1e9 numbers that could cause appr. errors. 
plt.plot(time,b,".")
plt.ylabel("Signal [A.U.]")
plt.xlabel("Time x10^9 [A.U]")
plt.savefig("time_series.png")
plt.clf()

# We set the design matrix to contain parameters for a third order parameter. 
A = np.zeros((len(t), 4))
A[:, 0] = 1.
A[:, 1] = t 
A[:, 2] = t**2
A[:, 3] = t**3
(u, w, vt) = np.linalg.svd(A, full_matrices=False)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(b)


cond_n=w[0]/w[-1]

print("The condition number for n=3 order polynomial is: ", cond_n)
bm = A.dot(x)
plt.plot(t, b, '.', label='Data')
plt.plot(t, bm, '-.', label='Model, third order polynomial (SVD)')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.savefig("t3.png")
plt.clf()


#### Let's compute residuals for Part C:
plt.plot(t,b-bm,".",label="Residuals")
plt.savefig("residuals.png")
plt.xlabel('Time')
plt.ylabel('Resiudals for the third order polynomial model')
plt.legend()
plt.savefig("residuals.png")
plt.clf()


## Part D: Higher order polynomial

n_order=20


A = np.zeros((len(t), n_order+1))

for n in np.arange(0,n_order+1):
    A[:, n] = t**n

(u, w, vt) = np.linalg.svd(A, full_matrices=False)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(b)

cond_n=w[0]/w[-1]

print(f"The condition number for n={n_order} order polynomial is: ", cond_n)
bm = A.dot(x)
plt.plot(t, b, '.', label='Data')
plt.plot(t, bm, '.', label='Model, 20th order polynomial (SVD)')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.savefig("model30.png")
plt.clf()

## Part D: Higher order fourier series model 
n_order=9
A = np.zeros((len(t), 2*n_order+1))

A[:, 0] = 1.
for n in np.arange(1,n_order+1):
    A[:, 2*n-1] = np.cos(n*t)
    A[:, 2*n] = np.sin(n*t)

(u, w, vt) = np.linalg.svd(A, full_matrices=False)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(b)

bm = A.dot(x)


cond_n=w[0]/w[-1]

print(f"The condition number for fourier series of order {2*n_order} is: ", cond_n)
plt.plot(t, b,'.', label='Data')
plt.plot(t, bm,'.', label=f'Model, Fourier series of order {2*n_order} (SVD)',alpha=0.3)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.savefig("fourier.png")
plt.clf()

## Finding the dominating harmonic:
Period_off_scale=0.15
Period_true_scale=(Period_off_scale*t_range)
print(Period_true_scale/31536000)
