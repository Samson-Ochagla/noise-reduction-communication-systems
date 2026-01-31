import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low')
    return lfilter(b, a, data)

# Signal setup
fs = 1000
t = np.arange(fs) / fs
signal = np.sin(2 * np.pi * 5 * t)
noise = np.random.normal(0, 0.5, signal.shape)
noisy_signal = signal + noise

filtered_signal = lowpass_filter(noisy_signal, cutoff=10, fs=fs)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label="Noisy Signal")
plt.plot(t, filtered_signal, label="Filtered Signal")
plt.legend()
plt.title("Low-Pass Filter Noise Reduction")
plt.show()
