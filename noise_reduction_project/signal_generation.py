import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
t = np.arange(fs) / fs
frequency = 5

# Clean signal
clean_signal = np.sin(2 * np.pi * frequency * t)

# Add white noise
noise = np.random.normal(0, 0.5, clean_signal.shape)
noisy_signal = clean_signal + noise

# Plot signals
plt.figure(figsize=(10, 6))
plt.plot(t, clean_signal, label="Clean Signal")
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.legend()
plt.title("Signal Generation with Noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
