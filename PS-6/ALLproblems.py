from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import timeit


### PART A ###
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
logwave=10**(logwave)


if True:
    flux=flux[:500] # Due to memory expensive computation, a subset of the samples is used during testing.    



if True: 
    plt.figure(figsize=(10,7))
    for i in np.arange(0,4):
        plt.plot(logwave,flux[i],".",label=f"Galaxy {i+1}")

    plt.xlabel("Wavelength, [Å]")
    plt.ylabel("Flux [10^-17 erg s^-1 cm^-2 Å-1]")
    plt.legend()
    plt.savefig(f"Galaxies.png")


### PART B ###
norms=np.array([])
for i,f in enumerate(flux):
    norm=np.sum(flux[i])
    norms=np.append(norms,norm)
    flux[i]=flux[i]/norm


if True:
    plt.figure(figsize=(10,7))
    for i in np.arange(0,4):
        plt.plot(logwave,flux[i],".",label=f"Galaxy {i+1}")

    plt.xlabel("Wavelength, [Å]")
    plt.ylabel("Flux [Norm units]")
    plt.legend()
    plt.savefig(f"Galaxies_norm.png")




### PART C ###

mean_values=np.array([])
for i,f in enumerate(flux):
    mean=np.mean(flux[i])
    mean_values=np.append(mean_values,mean)
    flux[i]=flux[i]-mean



if True:
    plt.figure(figsize=(10,7))
    for i in np.arange(0,4):
        plt.plot(logwave,flux[i],".",label=f"Galaxy {i+1}")

    plt.xlabel("Wavelength, [Å]")
    plt.ylabel("Flux around the mean [Norm. units]")
    plt.legend()
    plt.savefig(f"Galaxies_norm_mean.png")


### PART D ###
CovMatrix=np.dot(flux.T,flux) # Computing the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(CovMatrix)

print("Eigenvalues found")

# Plotting the eigenvectors:

plt.figure(figsize=(10,7))
for i in range(5):
    plt.plot(eigenvectors[:,i], label=f'Eigenvector {i+1}')

plt.ylabel("Eigenvector element size [A.U.]")
plt.xlabel("Eigenvector element")
plt.legend()
plt.savefig("eigen.png")
plt.clf()


### PART E ### 

(u, w, vt) = np.linalg.svd(flux)
svd_eigenvectors = vt.T
plt.figure(figsize=(10,7))
print("SVD U SHAPE",svd_eigenvectors.shape)
print("COV EIGENVECTOR shape",eigenvectors.shape)
for i in range(1,5):
    ### We test that the sign between eigenvectors are the same:
    dot_product=np.dot(svd_eigenvectors[:,i],eigenvectors[:,i])
    if dot_product>0:
        plt.plot(svd_eigenvectors[:,i]-eigenvectors[:,i], label=f'Residuals for Eigenvector #{i}')
    else:
        plt.plot(svd_eigenvectors[:,i]+eigenvectors[:,i], label=f'Residuals for Eigenvector #{i}')

plt.ylabel("Residual [A.U.]")
plt.xlabel("Eigenvector element")
plt.legend()
plt.savefig("eigen_residuals.png")
plt.clf()

### Let's time how fast the two eigenvector methods are. ###
if False: 
    execution_time_svd = timeit.timeit(lambda: np.linalg.svd(flux), number=1)
    print(f"It took {execution_time_svd} s to run the SVD method on R")
          
    execution_time_eig=timeit.timeit(lambda: np.linalg.eig(CovMatrix),number=1)
    print(f"It took {execution_time_eig} s to run the np.linalg eigenvalue method on C")


### PART F ###

# We now compute the condition number for R and C:

if True:
    (u, w, vt) = np.linalg.svd(CovMatrix)

    print("Cond C: ",w[0]/w[-1])

    (uf, wf, vtf) = np.linalg.svd(flux)
    print("Cond R: ",wf[0]/wf[-1])


### PART G ###

# We project the eigenvectors onto the data to get the PCA coefficients. 

PCA_coefficients=np.dot(flux,eigenvectors)
print(PCA_coefficients.shape)
# We now reproduce the spectrum using the first N principal components:
Nc=5
PCA_coefficients_N=PCA_coefficients[:,:Nc]
eigenvectors_N=eigenvectors[:,:Nc]
flux_reconstructed = np.dot(PCA_coefficients_N, eigenvectors_N.T)

if True:
    plt.figure(figsize=(10, 6))
    plt.plot(logwave, flux[0], label='Original Spectrum')
    plt.plot(logwave, flux_reconstructed[0], label=f'PCA (N={Nc})')
    plt.xlabel('Wavelength')
    plt.ylabel('Flux')
    plt.legend()
    plt.savefig("PCA.png")
    plt.clf()

### PART H ###
c0=PCA_coefficients[:,0]
c1=PCA_coefficients[:,1]
c2=PCA_coefficients[:,2]

if True:
    plt.figure(figsize=(10,6))
    plt.plot(c0,c1,".",label="C0 vs C1")
    plt.plot(c0,c2,".",label="C1 vs C2")
    plt.xlabel('Principal coefficient 0')
    plt.ylabel('Principal coefficient 1 and 2')
    plt.legend()
    plt.savefig("PCA_C.png")
    plt.clf()

### PART I ###
# We now compute the squared residuals as a function of number of PCA coefficients that we include. 
sq_residuals=[]
PCA_Nc=np.arange(1,21)
for Nc in PCA_Nc:
    sq_res=0
    PCA_coefficients_N=PCA_coefficients[:,:Nc]
    eigenvectors_N=eigenvectors[:,:Nc]
    flux_reconstructed = np.dot(PCA_coefficients_N, eigenvectors_N.T)
    for i in np.arange(len(flux[0])):
        sq_res+=np.square(flux[0][i]-flux_reconstructed[0][i])
    sq_residuals.append(sq_res)
    if Nc==20:
        print("Nc=20: ",np.sqrt(np.real(sq_residuals[-1]))/len(flux[0]))




plt.plot(PCA_Nc,sq_residuals,".",label="Squared residuals")
plt.xlabel("PCA_coefficients")
plt.ylabel("Squared resiudals")
plt.legend()
plt.savefig("Res_N.png")
plt.clf()

