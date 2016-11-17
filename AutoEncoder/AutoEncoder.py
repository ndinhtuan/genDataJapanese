#combine stochastic/ minibatch-gradient descent for autoencoder

from AutoLib import sigmoid, randWeight, ReLU, gradSig, gradReLU
import numpy as np
from .getData.getData import getData

data = getData("/home/tuan/Desktop/Katakana/train")
trainX = data[:, 0:data.shape[0]]
trainY = data[:, -1]
batch = 100
sizeInput = 50 * 50
sizeHidden = 200
m = data.shape[1] # size of training data
W1 = randWeight(sizeHidden, sizeInput)
b1 = randWeight(sizeHidden, 1)
W2 = randWeight(sizeInput, sizeHidden)
b2 = randWeight(sizeInput, 1)
decay = 3e-6
peta = 2e-3 # sparsity term
p = 0.05 #sparsity parameter
alpha = 0.01 #gradient parameter

#compute averange of training data in hidden layer
sumA2 = np.zeros((sizeHidden, 1))
for i in range(m) :

    z2 = W1 * X + b1
    a2 = ReLU(z2)
    sumA2 = sumA2 + a2

p2 = float(sumA2) / m

#run miniBatch
miniBatch = [trainX[:, k:k+batch] for k in range(0, m, batch)]

for i in len(miniBatch) :

    #forward to compute cost
    X = miniBatch[i]
    z2 = W1 * X + b1
    a2 = ReLU(z2)
    z3 = W2 * a2 + b2
    a3 = sigmoid(z3)

    cost = (1.0 / 2) * sum(sum( (a3 - X)**2 ))
    decayTerm = (decay / 2) * (sum(sum(W1**2)) + sum(b1**2) + sum(sum(W2**2)) + sum(b2**2))
    sparsityTerm = peta * (p * np.log2(p / p2) + (1 - p) * np.log2((1 - p) / (1 - p2)))
    J = cost + decayTerm + sparsityTerm
    print "cost : {}".format(J)

    # compute grad through backpropagation
    delta3 = (a3 - x) * gradSig(z3)
    gradSparity = peta * (-p / p2 + (1 - p) / (1 - p2))
    delta2 = (W2.T * delta3 + gradSparity) * gradReLU(z2)

    gradW1 = delta2 * X.T + decay * W1
    gradW2 = delta3 * a2.T + decay * W2
    gradb1 = sum(delta2.T).T
    gradb2 = sum(delta3.T).T

    #update
    W1 = W1 - alpha * gradW1
    W2 = W2 - alpha * gradW2
    b1 = b1 - alpha * gradb1
    b2 = b2 - alpha * gradb2

newTrainX = ReLU(W1 * trainX + b1)
