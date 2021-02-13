import numpy as np
import matplotlib.pyplot as plt
import random
from utils import sigmoid, activate, forward, calculateCost, loss
alpha = 6e-9


def predict(X,theta):
    X = np.array(X)
    X.reshape((1,7))
    return forward(X,theta)

def back_prop(prediction,X,theta):
    (n,m) = X.shape
    delta2 = np.transpose((predict(X,(theta1,theta2))-Y)@np.transpose(np.transpose(theta1)@X)/m)
    delta1 = X@(np.transpose(predict(X,(theta1,theta2))-Y))@np.transpose(theta2)
    theta1 = theta1 - alpha*delta1
    theta2 = theta2 - alpha*delta2
    cost = calculateCost(X,(theta1,theta2),Y)
    print(cost)
    # if cost > costs[-1]:
    #     print("DIVERGING")
    #     break
    costs.append(cost)