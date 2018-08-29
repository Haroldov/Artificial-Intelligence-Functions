import numpy as np
from cost import getCost
from scale import scaleData
import matplotlib.pyplot as plt
def logisticRegression(features, labels, iterations, learningRate, sw):
    features = scaleData(features).copy()
    X = np.concatenate((np.ones((np.size(features, axis=0),1)), features), axis=1)
    Y = labels
    m = np.size(X,axis=0) # number of samples
    theta = np.zeros((np.size(X, axis=1), 1))
    alpha = learningRate
    for i in range(1, iterations):
        theta = theta - (alpha/m)*(X.T@((1/(1+np.exp(-1*np.dot(theta.T, X.T))))-(Y.T)).T)
        cost = getCost(X,Y,theta)
        print('Error = ', np.asscalar(cost))
        # Hasta aquí termina el entrenamiento

    if sw == True: # La grafica
        [rng, tmp] = np.where(labels == 1)
        plt.plot(features[rng, 0], features[rng, 1], 'go',label = 'Clase 1')
        [rng, tmp] = np.where(labels == 0)
        plt.plot(features[rng, 0], features[rng, 1], 'bo',label = 'Clase 2')
        X2 = -1 * ((theta[0, 0] / theta[-1, 0]) + (theta[1, 0] / theta[-1, 0]) * features[:, 0])
        plt.plot(data[:, 0], X2, 'r',label = 'Limite de Decision')
        plt.xlabel('X1')
        plt.ylabel('Y1')
        plt.title('Grafica de Puntos')
        plt.legend()
        plt.show()

    return theta

