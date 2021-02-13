import random
import math

count = 0

# Env init
w,h = 500,200
fps = 60
hiscore = 0
bgColor = (0,180,255)
ground_color = (86,48,0)
rod_color = (150,90,0)

# Body Sizes
rod_length = 2*h/5
rod_thickness = 10
ground_height = h/5
datum = h-ground_height
# Basic physics
pi = math.pi
t = 1/fps/2
g = 5
a = 2*g

# Game variables / Kinematics Variables
theta = random.randint(-314,314)/400
omega = 0
alpha = 0
alpha_offset = 0
vel = 0
acc = 0
x = w/2
mu = 1

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