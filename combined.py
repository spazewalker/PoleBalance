import pygame
import pickle
import numpy as np
from game import init, iterate
from ann import NeuralNetwork
import utils

# Architecture (Specify archetecture here.)
network = NeuralNetwork(layers=[7,14,14,7,1],activations=['sigmoid','sigmoid','sigmoid','tanh'])
lr = 0.1
losses = []

screen,font = init()
# Game Loop / Train Loop
frame_count,score,_,_,x=iterate.iterate(screen,font,0,0)
game = True
run = True
prediction = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    prediction = utils.forward(x,network)
    frame_count,score,game,run,x = iterate.iterate(screen,font,frame_count,score,game,run,prediction)
    loss = utils.backward(prediction,x,lr,network)
    losses.append(loss)
pygame.quit()