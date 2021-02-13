import numpy as np
import random
import math

def findY(angle,score):
    print("Angle: ",angle*180/math.pi,score)
    temp = 2*(1/(1+np.exp(-5*(angle)))) - 1
    return -1 if temp>0.5 else 1 if temp<-0.5 else 0

def forward(x,network):
    x = np.array(x).reshape(7,1)
    z,a = network.forward_pass(x)
    value = a[-1].flatten().item()
    print("X: ",value)
    return 1 if value>0.5 else -1 if value<-0.5 else 0

def backward(prediction,x,lr,network):
    angle = x[2]
    score = x[6]
    y = findY(angle,score)
    print("Y: ",y)
    dw,db,loss = network.backward_pass(y)
    network.update(dw,db,lr)
    print("loss = {}".format(loss))
    return loss