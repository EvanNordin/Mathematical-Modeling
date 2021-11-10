#Defining an SIR system of differential equations
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

V0 = float(input("Enter the initial population of predators: "))
U0 = float(input("Enter the initial population of prey: "))
alpha = 0.1
t = np.linspace(0,100)

#Defining predator-prey as a function of time
def predPrey(y,t,alpha):
    U,V = y
    duDt = U*(1-V)
    dvDt = alpha*U*V - alpha*V
    return duDt, dvDt

#Specify y0 and then solve the system of differential equations, then plot   
y0 = U0,V0
y = odeint(predPrey, y0, t, args=(alpha,))
plt.plot(t,y)
plt.show()