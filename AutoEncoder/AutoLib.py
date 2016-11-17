import numpy as np

def randWeight(layerIn, layerOut) :

    epsilon = np.sqrt(6.0 / (layerIn + layerOut))
    weight = 2 * epsilon * np.random.rand(layerOut, layerIn) - epsilon
    return weight

def sigmoid(z):

    return 1.0 / (1.0 + np.exp(np.array(z)) )

def ReLU(z):

    return (z > 0) * z

def gradSig(z) :

    return (1 - sigmoid(z)) * sigmoid(z)

def gradReLU(z) :

    return (z > 0) * 1
