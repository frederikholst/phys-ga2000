import numpy as np
import matplotlib.pyplot as plt

# Set up parameters
num_samples = 1000  # Number of samples for each N
N_values = np.arange(1,400,10)  # Different values of N to test


# Plot setup
plt.figure(figsize=(10,8))
means=np.array([])
variances=np.array([])
kurtosis=np.array([])
skewness=np.array([])
for N in N_values:
    # Generate N exponentially distributed random variates per sample
    x = np.random.exponential(scale=1.0, size=(num_samples, N))
    
    y = np.mean(x, axis=1)
    

    #Update the skewness, variance and kurtosis arrays:
    means=np.append(means,np.mean(y))
    variances=np.append(variances,np.var(y))
    kurtosis = np.append(kurtosis,np.mean((y-np.mean(y))**4)/(np.mean((y-np.mean(y))**2)**2)-3)
    skewness = np.append(skewness, np.mean(((y - np.mean(y)) / np.std(y))**3))

    if N<52:
        plt.hist(y, bins=50, density=True, alpha=0.6, label=f'N = {N}')
    
        # Comparing with the theoretical Guassian
        mean_y = 1  
        std_y = np.sqrt(1 / N)  # Expected standard deviation
        x_vals = np.linspace(min(y), max(y), 1000)
        plt.plot(x_vals,1/(std_y*np.sqrt(2*np.pi))*np.exp(-(x_vals-mean_y)**2/(2*std_y**2)), 
                linestyle='dashdot')

# Add labels and title
plt.title('Distribution')
plt.xlabel('y')
plt.ylabel('Density')
plt.xlim((0,3.1))
plt.legend()
plt.savefig("gaus.png")

plt.clf()
plt.figure(figsize=(9,6))
plt.title("Features of the distribution")
plt.ylabel('Value of skew, kurtosis, mean and variance')
plt.xlabel('N')

plt.plot(N_values,means,label="Mean of y")
plt.plot(N_values,variances,label="Variance of y")
plt.plot(N_values,skewness,label="Skewness of y")
plt.plot(N_values,kurtosis,label="Kurtosis of y")

plt.legend()
plt.grid()
plt.savefig("distribution_feat.png")

# When is the skewness and kurtosis 1% of their maximum value at N=1?
thresh_skew=0.01*skewness[0]
N_value_skew=0
for i,s in enumerate(skewness):
    print(s)
    if s<thresh_skew:
        N_value_skew=N_values[i]
        break



thresh_kurt=0.01*kurtosis[0]
N_value_kurt=0
for i,k in enumerate(kurtosis):
    if k<thresh_kurt:
        N_value_kurt=N_values[i]
        break

print("N-value at 1 percent skewness is: ", N_value_skew," and the N value at 1% kurtosis: ", N_value_kurt)