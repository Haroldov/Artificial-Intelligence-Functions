import numpy as np
def getCost(X, Y, theta):
    m = np.size(X, axis=0)
    tmp = theta.T@X.T
    hypothesis = 1/(1+np.exp(-1*tmp))
    cost = (1/m)*(-1*Y.T@np.log10(hypothesis.T)-(1-Y.T)@np.log10(1-hypothesis.T))
    return cost
