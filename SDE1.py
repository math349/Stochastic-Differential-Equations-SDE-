import numpy as np
import matplotlib.pyplot as plt
# Parameters
dt = .001 # Time-step
sqrtdt = np.sqrt(dt)
T = 1 # Time limit
n = int(T / dt) # Total step
t = np.linspace(0., T, n) # Time step vector
x = np.zeros(n) #Simulation vectors and initial conditions
# the Euler-Maruyama Method
for i in range(n - 1):
    dW = sqrtdt*np.random.randn()
    x[i + 1] = x[i] + (2-x[i])*dt + x[i]*dW
#Plotting
plt.plot(t,x,label="the Euler-Maruyama Method",color="Red")
plt.legend()
plt.show()