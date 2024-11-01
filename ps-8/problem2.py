import numpy as np
import matplotlib.pyplot as plt


piano = np.genfromtxt('piano.csv', delimiter='\n')
trumpet = np.genfromtxt('trumpet.csv', delimiter='\n')

spectrum_p=np.fft.rfft(piano)
spectrum_t=np.fft.rfft(trumpet)
sample_r=44100
p_scaling_factor =sample_r/len(piano)
t_scaling_factor=sample_r/len(trumpet)


plt.plot(spectrum_p,".",label="Piano spectrum",alpha=0.6)
plt.plot(spectrum_t,".",label="Trumpet spectrum",alpha=0.6)
plt.legend()
plt.xlim(0,10000)
plt.savefig("pianotrumpet1.png")
plt.xlabel("Frequency [A.U.]")
plt.ylabel("Amplitude [A.U.]")
plt.show()
plt.clf()


frequency_series_p=np.arange(len(spectrum_p))*p_scaling_factor
frequency_series_t=np.arange(len(spectrum_t))*t_scaling_factor
plt.plot(frequency_series_p,spectrum_p,".",label="Piano spectrum",alpha=0.6)
plt.plot(frequency_series_t,spectrum_t,".",label="Trumpet spectrum",alpha=0.6)
plt.legend()
plt.xlim(0,1500)
plt.xlabel("Frequency, [Hz]")
plt.ylabel("Amplitude [A.U.]")
plt.savefig("C5.png")
plt.show()

frequency_max = frequency_series_p[np.argmax(spectrum_p)]
print(frequency_max)