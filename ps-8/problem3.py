import numpy as np
import matplotlib.pyplot as plt
dow=np.genfromtxt("dow.csv",delimiter="\n")
# PART A
plt.plot(dow,".")
plt.xlabel("Time since late 2006 [Days]")
plt.ylabel("Dow Jones Industrial Average [$]")
plt.savefig("dow.png")
plt.clf()
# PART B
coefficients=np.fft.rfft(dow)


# PART C
# Let's set everything but the first 10% to zero:
ten_percent_mark=int(0.10*len(coefficients))
coefficients[ten_percent_mark:] = 0
print(coefficients)

# PART D:
inverse_transform=np.fft.ifft(coefficients)
plt.plot(inverse_transform,".")
plt.xlabel("Time since late 2006 [Days]")
plt.ylabel("Dow Jones Industrial Average [$]")
plt.savefig("high_cut.png")
plt.clf()
# PART E
# Let's set everything but the first 2% to zero:
coefficients=np.fft.rfft(dow)
ten_percent_mark=int(0.02*len(coefficients))
coefficients[ten_percent_mark:] = 0


inverse_transform=np.fft.ifft(coefficients)
plt.plot(inverse_transform,".")
plt.xlabel("Time since late 2006 [Days]")
plt.ylabel("Dow Jones Industrial Average [$]")
plt.savefig("v_high_cut.png")
plt.clf()