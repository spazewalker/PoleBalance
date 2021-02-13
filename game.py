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

if __name__ == "__main__":
    screen,font = init()

    # Main Loop
    frame_count = 0
    score = 0
    game=True
    run=True
    while run:
        frame_count,score,game,run,_ = iterate.iterate(screen,font,frame_count,score,game,run)
    pygame.quit()