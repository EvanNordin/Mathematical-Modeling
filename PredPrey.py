#Defining an SIR system of differential equations
import sympy as sym


#Defining predator-prey as a function of time
def predPrey(y,t, alpha):
    U,V = y
    duDt = U(1-V)
    dvDt = alpha*U*V - alpha*V
    return duDt, dvDt
    