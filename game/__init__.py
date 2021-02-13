import pygame
import math
import game.iterate as iterate, game.config as config
import random

def init():
    # Game init
    pygame.init()
    screen = pygame.display.set_mode((config.w,config.h))
    pygame.display.set_caption("Balance")
    # Initialising Font and making base text for blitting
    font = pygame.font.Font('freesansbold.ttf', 32)
    return screen,font