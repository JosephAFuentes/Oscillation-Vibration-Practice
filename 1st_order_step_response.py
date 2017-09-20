'''TFirst order step Response and plotting
    DE: y'+5y = 1'''


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10)

y = 0.2-0.2*np.e**(-5*t)
plt.plot(t,y)
# Set y limits
plt.ylim(0, 0.3)

# Set y ticks
plt.yticks(np.linspace(0, 0.3, 10, endpoint=True))
plt.show()
