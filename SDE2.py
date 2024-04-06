import numpy as np
import matplotlib.pyplot as plt
# Parameters
s1 = 0.3 # Vasicek Standard Deviation
s2 = 0.3 # CIR Standard Deviation
K = 1 # a constant for both models
theta = 0.2 # a constant for both models
dt = .001 # Time-step
sqrtdt = np.sqrt(dt) 
T = 1 # Time limit
n = int(T / dt) # Total step
t = np.linspace(0., T, n) # Time step vector

xV = np.zeros(n); xC = np.zeros(n) #Simulation vectors and initial conditions
xV[0] = 0; xC[0] = 0 

SI = np.zeros(n)
#the Euler-Maruyama Method
for i in range(n - 1):
    dW = sqrtdt*np.random.randn()
    xV[i + 1] = xV[i] + dt*K*(theta-xV[i]) + s1*dW
    xC[i + 1] = xC[i] + dt*K*(theta -xC[i]) + s2*np.sqrt(xC[i])*dW
#Plotting
plt.plot(t,xV,label="Vasicek",color="Red")
plt.plot(t,xC,label="CIR",color="Blue")
plt.legend()
plt.show()