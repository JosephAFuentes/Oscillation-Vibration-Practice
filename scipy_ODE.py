'''m y''-(3x+2)y'+(6x-8)y=0, y(0)=2, y'(0)=3
'''
import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
m = 1
k = (2.0*np.pi)**2

wn = np.sqrt(k/m)       # Natural Frequency (rad/s)

z = 0.25                # Define a desired damping ratio
c = 2*z*wn*m 

def g(y, x):
    global m
    global c
    global k
    y0 = y[0]
    y1 = y[1]
    y2 = (c*(-y1)+k*(x))/(m)
    return y1, y2

# Initial conditions on y, y' at x=0
init = 0, 0
# First integrate from 0 to 2
x = np.linspace(0,2,100)
sol=odeint(g, init, x)
# Then integrate from 0 to -2
plt.plot(x, sol[:,0], color='b')
x = np.linspace(0,-2,100)
sol=odeint(g, init, x)
plt.plot(x, sol[:,0], color='b')

# The analytical answer in red dots
exact_x = np.linspace(-2,2,10)
exact_y = 2*np.exp(2*exact_x)-exact_x*np.exp(-exact_x)
plt.plot(exact_x,exact_y, 'o', color='r', label='exact')
plt.legend()

plt.show()
