import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def highpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high')
    return lfilter(b, a, data)

fs = 1000
t = np.arange(fs) / fs
signal = np.sin(2 * np.pi * 5 * t)
noise = np.random.normal(0, 0.5, signal.shape)
noisy_signal = signal + noise

filtered_signal = highpass_filter(noisy_signal, cutoff=1, fs=fs)

plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label="Noisy Signal")
plt.plot(t, filtered_signal, label="High-Pass Filtered Signal")
plt.legend()
plt.title("High-Pass Filter Noise Reduction")
plt.show()
