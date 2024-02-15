import matplotlib.pyplot as plt
import numpy as np
import math

e = math.e
pi = math.pi
x = np.linspace(0, 20, 100)
t = 2 * pi * x
cos = np.cos(t)

fig, axs = plt.subplots(3, 2, figsize=(12, 8))

axs[0, 0].plot(x, np.sin(x), label='sin(x)')
axs[0, 1].plot(x, e**(-0.5*x), label='e^(-0.5*x)')
axs[1, 0].plot(x, e**(0.5*x), label='e^(0.5*x)')
axs[1, 1].plot(x, e**(-0.5*x)*cos, label='e^(-0.5*x) * cos(2πx)')
axs[2, 0].plot(x, e**(0.5*x)*cos, label='e^(0.5*x) * cos(2πx)')

axs[2, 1].axis('off')

for ax in axs.flat:
    ax.legend()

plt.tight_layout()
plt.show()
