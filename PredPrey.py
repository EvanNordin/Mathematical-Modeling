#Defining an SIR system of differential equations
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Defining predator-prey as a function of time
def predPrey(y,t,alpha):
    U,V = y
    duDt = U*(1-V)
    dvDt = alpha*U*V - alpha*V
    return duDt, dvDt

#Setting up initial predator, prey, growth rate, and time values
U0 = float(input("Enter the initial population of prey: "))
V0 = float(input("Enter the initial population of predators: "))
alpha = float(input("Enter the alpha value: "))
t = np.linspace(0,100, num=1000)
#print(t)

#Specify y0 and then solve the system of differential equations, then plot   
y0 = U0,V0
y = odeint(predPrey, y0, t, args=(alpha,))
#print(y)

#Plot predator vs. prey in matplotlib with labeled axes
plt.plot(t,y)
plt.legend(["Prey", "Predator"])
plt.ylabel("Population")
plt.xlabel("Time")
plt.title("Predator VS. Prey Model w/ U_0={0}, V_0={1}, alpha={2}".format(U0, V0, alpha))

#Display plot
plt.show()
