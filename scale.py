import numpy as np
import numpy.matlib as ml
def scaleData(X):
    train = X.copy()
    xmax = np.amax(train,axis= 0)
    xmin = np.amin(train,axis = 0)
    output = (2 * (train - ml.repmat(xmin, np.size(train, axis=0), 1))/(ml.repmat(xmax, np.size(train, axis =0), 1) - ml.repmat(xmin, np.size(train, axis =0), 1)) - 1)
    return output